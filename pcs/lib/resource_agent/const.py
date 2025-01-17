from pcs.common.resource_agent import const

from .types import (
    _FAKE_AGENT_STANDARD,
    FakeAgentName,
    OcfVersion,
)

OCF_1_0 = OcfVersion("1.0")
OCF_1_1 = OcfVersion("1.1")
SUPPORTED_OCF_VERSIONS = [OCF_1_0, OCF_1_1]

FAKE_AGENT_STANDARD = _FAKE_AGENT_STANDARD
PACEMAKER_FENCED = FakeAgentName("pacemaker-fenced")

STONITH_ACTION_REPLACED_BY = ["pcmk_off_action", "pcmk_reboot_action"]
DEFAULT_UNIQUE_GROUP_PREFIX = const.DEFAULT_UNIQUE_GROUP_PREFIX
