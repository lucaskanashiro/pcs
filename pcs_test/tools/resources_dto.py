"""
Data structures in this file correspond to resources configured in
pcs_test/resources/cib-resources.xml
"""
from pcs.common.pacemaker.nvset import (
    CibNvpairDto,
    CibNvsetDto,
)
from pcs.common.pacemaker.resource.bundle import (
    CibResourceBundleContainerRuntimeOptionsDto,
    CibResourceBundleDto,
    CibResourceBundleNetworkOptionsDto,
    CibResourceBundlePortMappingDto,
    CibResourceBundleStorageMappingDto,
)
from pcs.common.pacemaker.resource.clone import CibResourceCloneDto
from pcs.common.pacemaker.resource.group import CibResourceGroupDto
from pcs.common.pacemaker.resource.list import ListCibResourcesDto
from pcs.common.pacemaker.resource.operations import CibResourceOperationDto
from pcs.common.pacemaker.resource.primitive import CibResourcePrimitiveDto
from pcs.common.resource_agent.dto import ResourceAgentNameDto

DUMMY_AGENT_NAME = ResourceAgentNameDto(
    standard="ocf", provider="pacemaker", type="Dummy"
)

STONITH_AGENT_NAME = ResourceAgentNameDto(
    standard="stonith", provider=None, type="fence_kdump"
)


def _primitive_fixture(primitive_id, agent_name=DUMMY_AGENT_NAME):
    return CibResourcePrimitiveDto(
        id=primitive_id,
        agent_name=agent_name,
        description=None,
        operations=[
            CibResourceOperationDto(
                id=f"{primitive_id}-monitor-interval-10s",
                name="monitor",
                interval="10s",
                description=None,
                start_delay=None,
                interval_origin=None,
                timeout="20s",
                enabled=None,
                record_pending=None,
                role=None,
                on_fail=None,
                meta_attributes=[],
                instance_attributes=[],
            )
        ],
        meta_attributes=[],
        instance_attributes=[],
        utilization=[],
    )


PRIMITIVE_R1 = _primitive_fixture("R1")
PRIMITIVE_R2 = _primitive_fixture("R2")
PRIMITIVE_R3 = _primitive_fixture("R3")
PRIMITIVE_R4 = _primitive_fixture("R4")
PRIMITIVE_R5 = _primitive_fixture("R5")
PRIMITIVE_R6 = CibResourcePrimitiveDto(
    id="R6",
    agent_name=DUMMY_AGENT_NAME,
    description=None,
    operations=[
        CibResourceOperationDto(
            id="R6-migrate_from-interval-0s",
            name="migrate_from",
            interval="0s",
            description=None,
            start_delay=None,
            interval_origin=None,
            timeout="20s",
            enabled=None,
            record_pending=None,
            role=None,
            on_fail=None,
            meta_attributes=[],
            instance_attributes=[],
        ),
        CibResourceOperationDto(
            id="R6-migrate_to-interval-0s",
            name="migrate_to",
            interval="0s",
            description=None,
            start_delay=None,
            interval_origin=None,
            timeout="20s",
            enabled=None,
            record_pending=None,
            role=None,
            on_fail=None,
            meta_attributes=[],
            instance_attributes=[],
        ),
        CibResourceOperationDto(
            id="R6-monitor-interval-10s",
            name="monitor",
            interval="10s",
            description=None,
            start_delay=None,
            interval_origin=None,
            timeout="20s",
            enabled=None,
            record_pending=None,
            role=None,
            on_fail=None,
            meta_attributes=[],
            instance_attributes=[],
        ),
        CibResourceOperationDto(
            id="R6-reload-interval-0s",
            name="reload",
            interval="0s",
            description=None,
            start_delay=None,
            interval_origin=None,
            timeout="20s",
            enabled=None,
            record_pending=None,
            role=None,
            on_fail=None,
            meta_attributes=[],
            instance_attributes=[],
        ),
        CibResourceOperationDto(
            id="R6-reload-agent-interval-0s",
            name="reload-agent",
            interval="0s",
            description=None,
            start_delay=None,
            interval_origin=None,
            timeout="20s",
            enabled=None,
            record_pending=None,
            role=None,
            on_fail=None,
            meta_attributes=[],
            instance_attributes=[],
        ),
        CibResourceOperationDto(
            id="R6-start-interval-0s",
            name="start",
            interval="0s",
            description=None,
            start_delay=None,
            interval_origin=None,
            timeout="20s",
            enabled=None,
            record_pending=None,
            role=None,
            on_fail=None,
            meta_attributes=[],
            instance_attributes=[],
        ),
        CibResourceOperationDto(
            id="R6-stop-interval-0s",
            name="stop",
            interval="0s",
            description=None,
            start_delay=None,
            interval_origin=None,
            timeout="20s",
            enabled=None,
            record_pending=None,
            role=None,
            on_fail=None,
            meta_attributes=[],
            instance_attributes=[],
        ),
    ],
    meta_attributes=[],
    instance_attributes=[],
    utilization=[],
)
PRIMITIVE_R7 = CibResourcePrimitiveDto(
    id="R7",
    agent_name=DUMMY_AGENT_NAME,
    description=None,
    operations=[
        CibResourceOperationDto(
            id="R7-custom_action-interval-10s",
            name="custom_action",
            interval="10s",
            description=None,
            start_delay=None,
            interval_origin=None,
            timeout=None,
            enabled=None,
            record_pending=None,
            role=None,
            on_fail=None,
            meta_attributes=[],
            instance_attributes=[
                CibNvsetDto(
                    id="R7-custom_action-interval-10s-instance_attributes",
                    options={},
                    rule=None,
                    nvpairs=[
                        CibNvpairDto(
                            id="R7-custom_action-interval-10s-instance_attributes-OCF_CHECK_LEVEL",
                            name="OCF_CHECK_LEVEL",
                            value="2",
                        )
                    ],
                )
            ],
        ),
        CibResourceOperationDto(
            id="R7-migrate_from-interval-0s",
            name="migrate_from",
            interval="0s",
            description=None,
            start_delay=None,
            interval_origin=None,
            timeout="20s",
            enabled=None,
            record_pending=None,
            role=None,
            on_fail=None,
            meta_attributes=[],
            instance_attributes=[],
        ),
        CibResourceOperationDto(
            id="R7-migrate_to-interval-0s",
            name="migrate_to",
            interval="0s",
            description=None,
            start_delay=None,
            interval_origin=None,
            timeout="20s",
            enabled=None,
            record_pending=None,
            role=None,
            on_fail=None,
            meta_attributes=[],
            instance_attributes=[],
        ),
        CibResourceOperationDto(
            id="R7-monitor-interval-10s",
            name="monitor",
            interval="10s",
            description=None,
            start_delay=None,
            interval_origin=None,
            timeout="20s",
            enabled=None,
            record_pending=None,
            role=None,
            on_fail=None,
            meta_attributes=[],
            instance_attributes=[],
        ),
        CibResourceOperationDto(
            id="R7-reload-interval-0s",
            name="reload",
            interval="0s",
            description=None,
            start_delay=None,
            interval_origin=None,
            timeout="20s",
            enabled=None,
            record_pending=None,
            role=None,
            on_fail=None,
            meta_attributes=[],
            instance_attributes=[],
        ),
        CibResourceOperationDto(
            id="R7-reload-agent-interval-0s",
            name="reload-agent",
            interval="0s",
            description=None,
            start_delay=None,
            interval_origin=None,
            timeout="20s",
            enabled=None,
            record_pending=None,
            role=None,
            on_fail=None,
            meta_attributes=[],
            instance_attributes=[],
        ),
        CibResourceOperationDto(
            id="R7-start-interval-0s",
            name="start",
            interval="0s",
            description=None,
            start_delay=None,
            interval_origin=None,
            timeout="20s",
            enabled=None,
            record_pending=None,
            role=None,
            on_fail=None,
            meta_attributes=[],
            instance_attributes=[],
        ),
        CibResourceOperationDto(
            id="R7-stop-interval-0s",
            name="stop",
            interval="0s",
            description=None,
            start_delay=None,
            interval_origin=None,
            timeout="20s",
            enabled=None,
            record_pending=None,
            role=None,
            on_fail=None,
            meta_attributes=[],
            instance_attributes=[],
        ),
    ],
    meta_attributes=[
        CibNvsetDto(
            id="R7-meta_attributes",
            options={},
            rule=None,
            nvpairs=[
                CibNvpairDto(
                    id="R7-meta_attributes-anotherone",
                    name="anotherone",
                    value="something'\"special",
                ),
                CibNvpairDto(
                    id="R7-meta_attributes-anotherone0",
                    name="another one0",
                    value="a + b = c",
                ),
                CibNvpairDto(
                    id="R7-meta_attributes-m1",
                    name="m1",
                    value="value1",
                ),
                CibNvpairDto(
                    id="R7-meta_attributes-m10",
                    name="m10",
                    value="value1",
                ),
                CibNvpairDto(
                    id="R7-meta_attributes-meta2",
                    name="meta2",
                    value="valueofmeta2isthisverylongstring",
                ),
                CibNvpairDto(
                    id="R7-meta_attributes-meta20",
                    name="meta20",
                    value="valueofmeta2isthisverylongstring",
                ),
            ],
        )
    ],
    instance_attributes=[
        CibNvsetDto(
            id="R7-instance_attributes",
            options={},
            rule=None,
            nvpairs=[
                CibNvpairDto(
                    id="R7-instance_attributes-envfile",
                    name="envfile",
                    value="/dev/null",
                ),
                CibNvpairDto(
                    id="R7-instance_attributes-fake",
                    name="fake",
                    value="looool",
                ),
            ],
        )
    ],
    utilization=[],
)
STONITH_S1 = CibResourcePrimitiveDto(
    id="S1",
    agent_name=STONITH_AGENT_NAME,
    description=None,
    operations=[
        CibResourceOperationDto(
            id="S1-monitor-interval-60s",
            name="monitor",
            interval="60s",
            description=None,
            start_delay=None,
            interval_origin=None,
            timeout=None,
            enabled=None,
            record_pending=None,
            role=None,
            on_fail=None,
            meta_attributes=[],
            instance_attributes=[],
        )
    ],
    meta_attributes=[],
    instance_attributes=[
        CibNvsetDto(
            id="S1-instance_attributes",
            options={},
            rule=None,
            nvpairs=[
                CibNvpairDto(
                    id="S1-instance_attributes-nodename",
                    name="nodename",
                    value="testnodename",
                )
            ],
        )
    ],
    utilization=[],
)
STONITH_S2 = CibResourcePrimitiveDto(
    id="S2",
    agent_name=STONITH_AGENT_NAME,
    description=None,
    operations=[
        CibResourceOperationDto(
            id="S2-monitor-interval-60s",
            name="monitor",
            interval="60s",
            description=None,
            start_delay=None,
            interval_origin=None,
            timeout=None,
            enabled=None,
            record_pending=None,
            role=None,
            on_fail=None,
            meta_attributes=[],
            instance_attributes=[],
        )
    ],
    meta_attributes=[],
    instance_attributes=[],
    utilization=[],
)
CLONE_G1 = CibResourceCloneDto(
    id="G1-clone",
    description=None,
    member_id="G1",
    meta_attributes=[
        CibNvsetDto(
            id="G1-clone-meta_attributes",
            options={},
            rule=None,
            nvpairs=[
                CibNvpairDto(
                    id="G1-clone-meta_attributes-promotable",
                    name="promotable",
                    value="true",
                )
            ],
        )
    ],
    instance_attributes=[],
)
CLONE_R6 = CibResourceCloneDto(
    id="R6-clone",
    description=None,
    member_id="R6",
    meta_attributes=[],
    instance_attributes=[],
)
GROUP_G1 = CibResourceGroupDto(
    id="G1",
    description=None,
    member_ids=["R2", "R3", "R4"],
    meta_attributes=[],
    instance_attributes=[],
)
GROUP_G2 = CibResourceGroupDto(
    id="G2",
    description=None,
    member_ids=["R5", "S1"],
    meta_attributes=[
        CibNvsetDto(
            id="G2-meta_attributes",
            options={},
            rule=None,
            nvpairs=[
                CibNvpairDto(
                    id="G2-meta_attributes-meta1",
                    name="meta1",
                    value="metaval1",
                ),
                CibNvpairDto(
                    id="G2-meta_attributes-meta2",
                    name="meta2",
                    value="metaval2",
                ),
            ],
        )
    ],
    instance_attributes=[],
)
BUNDLE_B1 = CibResourceBundleDto(
    id="B1",
    description=None,
    member_id=None,
    container_type="docker",
    container_options=CibResourceBundleContainerRuntimeOptionsDto(
        image="pcs:test",
        replicas=4,
        replicas_per_host=2,
        promoted_max=None,
        run_command="/bin/true",
        network="extra_network_settings",
        options="extra_options",
    ),
    network=CibResourceBundleNetworkOptionsDto(
        ip_range_start="192.168.100.200",
        control_port=12345,
        host_interface="eth0",
        host_netmask=24,
        add_host=None,
    ),
    port_mappings=[
        CibResourceBundlePortMappingDto(
            id="B1-port-map-1001",
            port=1001,
            internal_port=None,
            range=None,
        ),
        CibResourceBundlePortMappingDto(
            id="B1-port-map-2000",
            port=2000,
            internal_port=2002,
            range=None,
        ),
        CibResourceBundlePortMappingDto(
            id="B1-port-map-3000-3300",
            port=None,
            internal_port=None,
            range="3000-3300",
        ),
    ],
    storage_mappings=[
        CibResourceBundleStorageMappingDto(
            id="B1-storage-map",
            source_dir="/tmp/docker1a",
            source_dir_root=None,
            target_dir="/tmp/docker1b",
            options=None,
        ),
        CibResourceBundleStorageMappingDto(
            id="B1-storage-map-1",
            source_dir="/tmp/docker2a",
            source_dir_root=None,
            target_dir="/tmp/docker2b",
            options=None,
        ),
        CibResourceBundleStorageMappingDto(
            id="B1-storage-map-2",
            source_dir=None,
            source_dir_root="/tmp/docker3a",
            target_dir="/tmp/docker3b",
            options=None,
        ),
        CibResourceBundleStorageMappingDto(
            id="B1-storage-map-3",
            source_dir=None,
            source_dir_root="/tmp/docker4a",
            target_dir="/tmp/docker4b",
            options=None,
        ),
    ],
    meta_attributes=[
        CibNvsetDto(
            id="B1-meta_attributes",
            options={},
            rule=None,
            nvpairs=[
                CibNvpairDto(
                    id="B1-meta_attributes-is-managed",
                    name="is-managed",
                    value="false",
                ),
                CibNvpairDto(
                    id="B1-meta_attributes-target-role",
                    name="target-role",
                    value="Stopped",
                ),
            ],
        )
    ],
    instance_attributes=[],
)
BUNDLE_B2 = CibResourceBundleDto(
    id="B2",
    description=None,
    member_id="R1",
    container_type="docker",
    container_options=CibResourceBundleContainerRuntimeOptionsDto(
        image="pcs:test",
        replicas=None,
        replicas_per_host=None,
        promoted_max=None,
        run_command=None,
        network=None,
        options=None,
    ),
    network=None,
    port_mappings=[],
    storage_mappings=[],
    meta_attributes=[],
    instance_attributes=[],
)

ALL_RESOURCES = ListCibResourcesDto(
    primitives=[
        PRIMITIVE_R1,
        PRIMITIVE_R7,
        STONITH_S2,
        PRIMITIVE_R5,
        STONITH_S1,
        PRIMITIVE_R2,
        PRIMITIVE_R3,
        PRIMITIVE_R4,
        PRIMITIVE_R6,
    ],
    clones=[
        CLONE_G1,
        CLONE_R6,
    ],
    groups=[
        GROUP_G2,
        GROUP_G1,
    ],
    bundles=[
        BUNDLE_B1,
        BUNDLE_B2,
    ],
)