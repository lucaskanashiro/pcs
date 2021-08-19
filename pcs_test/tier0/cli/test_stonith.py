from unittest import mock, TestCase

from pcs import stonith
from pcs.common import reports
from pcs.cli.common.errors import CmdLineInputError
from pcs.cli.common.parse_args import InputModifiers

from pcs_test.tools.misc import dict_to_modifiers


def _dict_to_modifiers(options):
    def _convert_val(val):
        if val is True:
            return ""
        return val

    return InputModifiers(
        {
            f"--{opt}": _convert_val(val)
            for opt, val in options.items()
            if val is not False
        }
    )


class SbdEnable(TestCase):
    def setUp(self):
        self.lib = mock.Mock(spec_set=["sbd"])
        self.sbd = mock.Mock(spec_set=["enable_sbd"])
        self.lib.sbd = self.sbd

    def assert_called_with(
        self, default_watchdog, watchdog_dict, sbd_options, **kwargs
    ):
        default_kwargs = dict(
            default_device_list=None,
            node_device_dict=None,
            allow_unknown_opts=False,
            ignore_offline_nodes=False,
            no_watchdog_validation=False,
        )
        default_kwargs.update(kwargs)
        self.sbd.enable_sbd.assert_called_once_with(
            default_watchdog, watchdog_dict, sbd_options, **default_kwargs
        )

    def call_cmd(self, argv, modifiers=None):
        stonith.sbd_enable(self.lib, argv, _dict_to_modifiers(modifiers or {}))

    def test_no_args(self):
        self.call_cmd([])
        self.assert_called_with(None, dict(), dict())

    def test_watchdog(self):
        self.call_cmd(["watchdog=/dev/wd"])
        self.assert_called_with("/dev/wd", dict(), dict())

    def test_device(self):
        self.call_cmd(["device=/dev/sda"])
        self.assert_called_with(
            None, dict(), dict(), default_device_list=["/dev/sda"]
        )

    def test_options(self):
        self.call_cmd(["SBD_A=a", "SBD_B=b"])
        self.assert_called_with(None, dict(), dict(SBD_A="a", SBD_B="b"))

    def test_multiple_watchdogs_devices(self):
        self.call_cmd(
            [
                "watchdog=/dev/wd",
                "watchdog=/dev/wda@node-a",
                "watchdog=/dev/wdb@node-b",
                "device=/dev/sda1",
                "device=/dev/sda2",
                "device=/dev/sdb1@node-b",
                "device=/dev/sdb2@node-b",
                "device=/dev/sdc1@node-c",
                "device=/dev/sdc2@node-c",
            ]
        )
        self.assert_called_with(
            "/dev/wd",
            {"node-a": "/dev/wda", "node-b": "/dev/wdb"},
            dict(),
            default_device_list=["/dev/sda1", "/dev/sda2"],
            node_device_dict={
                "node-b": ["/dev/sdb1", "/dev/sdb2"],
                "node-c": ["/dev/sdc1", "/dev/sdc2"],
            },
        )

    def test_modifiers(self):
        self.call_cmd(
            [],
            modifiers={
                "force": "",
                "skip-offline": "",
                "no-watchdog-validation": "",
            },
        )
        self.assert_called_with(
            None,
            dict(),
            dict(),
            allow_unknown_opts=True,
            ignore_offline_nodes=True,
            no_watchdog_validation=True,
        )


class SbdDeviceSetup(TestCase):
    def setUp(self):
        self.lib = mock.Mock(spec_set=["sbd"])
        self.sbd = mock.Mock(spec_set=["initialize_block_devices"])
        self.lib.sbd = self.sbd

    def assert_called_with(self, device_list, option_dict):
        self.sbd.initialize_block_devices.assert_called_once_with(
            device_list, option_dict
        )

    def call_cmd(self, argv, modifiers=None):
        all_modifiers = dict(
            force=True,  # otherwise it asks interactively for confirmation
        )
        all_modifiers.update(modifiers or {})
        stonith.sbd_setup_block_device(
            self.lib, argv, _dict_to_modifiers(all_modifiers)
        )

    def test_no_args(self):
        with self.assertRaises(CmdLineInputError) as cm:
            self.call_cmd([])
        self.assertEqual(cm.exception.message, "No device defined")

    @mock.patch("pcs.cli.reports.output.warn")
    def test_minimal(self, mock_warn):
        self.call_cmd(["device=/dev/sda"])
        self.assert_called_with(["/dev/sda"], dict())
        mock_warn.assert_called_once_with(
            "All current content on device(s) '/dev/sda' will be overwritten"
        )

    @mock.patch("pcs.cli.reports.output.warn")
    def test_devices_and_options(self, mock_warn):
        self.call_cmd(["device=/dev/sda", "a=A", "device=/dev/sdb", "b=B"])
        self.assert_called_with(["/dev/sda", "/dev/sdb"], {"a": "A", "b": "B"})
        mock_warn.assert_called_once_with(
            "All current content on device(s) '/dev/sda', '/dev/sdb' will be "
            "overwritten"
        )

    def test_options(self):
        with self.assertRaises(CmdLineInputError) as cm:
            self.call_cmd(["a=A"])
        self.assertEqual(cm.exception.message, "No device defined")


class StonithUpdateScsiDevices(TestCase):
    def setUp(self):
        self.lib = mock.Mock(spec_set=["stonith"])
        self.stonith = mock.Mock(spec_set=["update_scsi_devices"])
        self.lib.stonith = self.stonith

    def assert_called_with(self, stonith_id, set_devices, force_flags):
        self.stonith.update_scsi_devices.assert_called_once_with(
            stonith_id, set_devices, force_flags=force_flags
        )

    def call_cmd(self, argv, modifiers=None):
        stonith.stonith_update_scsi_devices(
            self.lib, argv, dict_to_modifiers(modifiers or {})
        )

    def test_no_args(self):
        with self.assertRaises(CmdLineInputError) as cm:
            self.call_cmd([])
        self.assertEqual(cm.exception.message, None)

    def test_only_stonith_id(self):
        with self.assertRaises(CmdLineInputError) as cm:
            self.call_cmd(["stonith-id"])
        self.assertEqual(cm.exception.message, None)

    def test_not_set_keyword(self):
        with self.assertRaises(CmdLineInputError) as cm:
            self.call_cmd(["stonith-id", "unset"])
        self.assertEqual(cm.exception.message, None)

    def test_only_set_keyword(self):
        with self.assertRaises(CmdLineInputError) as cm:
            self.call_cmd(["stonith-id", "set"])
        self.assertEqual(cm.exception.message, None)
        self.assertEqual(
            cm.exception.hint, "You must specify set devices to be updated"
        )

    def test_one_device(self):
        self.call_cmd(["stonith-id", "set", "device1"])
        self.assert_called_with("stonith-id", ["device1"], [])

    def test_more_devices(self):
        self.call_cmd(["stonith-id", "set", "device1", "device2"])
        self.assert_called_with("stonith-id", ["device1", "device2"], [])

    def test_supported_options(self):
        self.call_cmd(
            ["stonith-id", "set", "device1", "device2"],
            {"skip-offline": True, "request-timeout": 60},
        )
        self.assert_called_with(
            "stonith-id",
            ["device1", "device2"],
            [reports.codes.SKIP_OFFLINE_NODES],
        )

    def test_unsupported_options(self):
        with self.assertRaises(CmdLineInputError) as cm:
            self.call_cmd(
                ["stonith-id", "set", "device1", "device2"], {"force": True}
            )
        self.assertEqual(
            cm.exception.message,
            "Specified option '--force' is not supported in this command",
        )
