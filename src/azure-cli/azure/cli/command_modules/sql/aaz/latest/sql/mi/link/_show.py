# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
#
# Code generated by aaz-dev-tools
# --------------------------------------------------------------------------------------------

# pylint: skip-file
# flake8: noqa

from azure.cli.core.aaz import *


@register_command(
    "sql mi link show",
)
class Show(AAZCommand):
    """Get a distributed availability group info.
    """

    _aaz_info = {
        "version": "2022-02-01-preview",
        "resources": [
            ["mgmt-plane", "/subscriptions/{}/resourcegroups/{}/providers/microsoft.sql/managedinstances/{}/distributedavailabilitygroups/{}", "2022-02-01-preview"],
        ]
    }

    def _handler(self, command_args):
        super()._handler(command_args)
        self._execute_operations()
        return self._output()

    _args_schema = None

    @classmethod
    def _build_arguments_schema(cls, *args, **kwargs):
        if cls._args_schema is not None:
            return cls._args_schema
        cls._args_schema = super()._build_arguments_schema(*args, **kwargs)

        # define Arg Group ""

        _args_schema = cls._args_schema
        _args_schema.distributed_availability_group_name = AAZStrArg(
            options=["-n", "--name", "--distributed-availability-group-name"],
            help="Distributed availability group name.",
            required=True,
            id_part="child_name_1",
        )
        _args_schema.managed_instance_name = AAZStrArg(
            options=["--mi", "--instance-name", "--managed-instance", "--managed-instance-name"],
            help="Name of the managed instance.",
            required=True,
            id_part="name",
        )
        _args_schema.resource_group = AAZResourceGroupNameArg(
            required=True,
        )
        return cls._args_schema

    def _execute_operations(self):
        self.DistributedAvailabilityGroupsGet(ctx=self.ctx)()

    def _output(self, *args, **kwargs):
        result = self.deserialize_output(self.ctx.vars.instance, client_flatten=True)
        return result

    class DistributedAvailabilityGroupsGet(AAZHttpOperation):
        CLIENT_TYPE = "MgmtClient"

        def __call__(self, *args, **kwargs):
            request = self.make_request()
            session = self.client.send_request(request=request, stream=False, **kwargs)
            if session.http_response.status_code in [200]:
                return self.on_200(session)

            return self.on_error(session.http_response)

        @property
        def url(self):
            return self.client.format_url(
                "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Sql/managedInstances/{managedInstanceName}/distributedAvailabilityGroups/{distributedAvailabilityGroupName}",
                **self.url_parameters
            )

        @property
        def method(self):
            return "GET"

        @property
        def error_format(self):
            return "ODataV4Format"

        @property
        def url_parameters(self):
            parameters = {
                **self.serialize_url_param(
                    "distributedAvailabilityGroupName", self.ctx.args.distributed_availability_group_name,
                    required=True,
                ),
                **self.serialize_url_param(
                    "managedInstanceName", self.ctx.args.managed_instance_name,
                    required=True,
                ),
                **self.serialize_url_param(
                    "resourceGroupName", self.ctx.args.resource_group,
                    required=True,
                ),
                **self.serialize_url_param(
                    "subscriptionId", self.ctx.subscription_id,
                    required=True,
                ),
            }
            return parameters

        @property
        def query_parameters(self):
            parameters = {
                **self.serialize_query_param(
                    "api-version", "2022-02-01-preview",
                    required=True,
                ),
            }
            return parameters

        @property
        def header_parameters(self):
            parameters = {
                **self.serialize_header_param(
                    "Accept", "application/json",
                ),
            }
            return parameters

        def on_200(self, session):
            data = self.deserialize_http_content(session)
            self.ctx.set_var(
                "instance",
                data,
                schema_builder=self._build_schema_on_200
            )

        _schema_on_200 = None

        @classmethod
        def _build_schema_on_200(cls):
            if cls._schema_on_200 is not None:
                return cls._schema_on_200

            cls._schema_on_200 = AAZObjectType()

            _schema_on_200 = cls._schema_on_200
            _schema_on_200.id = AAZStrType(
                flags={"read_only": True},
            )
            _schema_on_200.name = AAZStrType(
                flags={"read_only": True},
            )
            _schema_on_200.properties = AAZObjectType(
                flags={"client_flatten": True},
            )
            _schema_on_200.type = AAZStrType(
                flags={"read_only": True},
            )

            properties = cls._schema_on_200.properties
            properties.distributed_availability_group_id = AAZStrType(
                serialized_name="distributedAvailabilityGroupId",
                flags={"read_only": True},
            )
            properties.last_hardened_lsn = AAZStrType(
                serialized_name="lastHardenedLsn",
                flags={"read_only": True},
            )
            properties.link_state = AAZStrType(
                serialized_name="linkState",
                flags={"read_only": True},
            )
            properties.primary_availability_group_name = AAZStrType(
                serialized_name="primaryAvailabilityGroupName",
            )
            properties.replication_mode = AAZStrType(
                serialized_name="replicationMode",
            )
            properties.secondary_availability_group_name = AAZStrType(
                serialized_name="secondaryAvailabilityGroupName",
            )
            properties.source_endpoint = AAZStrType(
                serialized_name="sourceEndpoint",
            )
            properties.source_replica_id = AAZStrType(
                serialized_name="sourceReplicaId",
                flags={"read_only": True},
            )
            properties.target_database = AAZStrType(
                serialized_name="targetDatabase",
            )
            properties.target_replica_id = AAZStrType(
                serialized_name="targetReplicaId",
                flags={"read_only": True},
            )

            return cls._schema_on_200


__all__ = ["Show"]
