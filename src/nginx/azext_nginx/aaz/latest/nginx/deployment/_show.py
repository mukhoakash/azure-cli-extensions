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
    "nginx deployment show",
)
class Show(AAZCommand):
    """Get the properties of a specific Nginx Deployment

    :example: Deployment Get
        az nginx deployment show --name myDeployment --resource-group myResourceGroup
    """

    _aaz_info = {
        "version": "2022-08-01",
        "resources": [
            ["mgmt-plane", "/subscriptions/{}/resourcegroups/{}/providers/nginx.nginxplus/nginxdeployments/{}", "2022-08-01"],
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
        _args_schema.deployment_name = AAZStrArg(
            options=["-n", "--name", "--deployment-name"],
            help="The name of targeted Nginx deployment",
            required=True,
            id_part="name",
        )
        _args_schema.resource_group = AAZResourceGroupNameArg(
            required=True,
        )
        return cls._args_schema

    def _execute_operations(self):
        self.DeploymentsGet(ctx=self.ctx)()

    def _output(self, *args, **kwargs):
        result = self.deserialize_output(self.ctx.vars.instance, client_flatten=True)
        return result

    class DeploymentsGet(AAZHttpOperation):
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
                "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Nginx.NginxPlus/nginxDeployments/{deploymentName}",
                **self.url_parameters
            )

        @property
        def method(self):
            return "GET"

        @property
        def error_format(self):
            return "ODataV4Format"

        @property
        def query_parameters(self):
            parameters = {
                **self.serialize_query_param(
                    "api-version", "2022-08-01",
                    required=True,
                ),
            }
            return parameters
            
        @property
        def url_parameters(self):
            parameters = {
                **self.serialize_url_param(
                    "deploymentName", self.ctx.args.deployment_name,
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
            _schema_on_200.identity = AAZObjectType()
            _schema_on_200.location = AAZStrType()
            _schema_on_200.name = AAZStrType(
                flags={"read_only": True},
            )
            _schema_on_200.properties = AAZObjectType()
            _schema_on_200.sku = AAZObjectType()
            _schema_on_200.system_data = AAZObjectType(
                serialized_name="systemData",
                flags={"read_only": True},
            )
            _schema_on_200.tags = AAZDictType()
            _schema_on_200.type = AAZStrType(
                flags={"read_only": True},
            )

            identity = cls._schema_on_200.identity
            identity.principal_id = AAZStrType(
                serialized_name="principalId",
                flags={"read_only": True},
            )
            identity.tenant_id = AAZStrType(
                serialized_name="tenantId",
                flags={"read_only": True},
            )
            identity.type = AAZStrType()
            identity.user_assigned_identities = AAZDictType(
                serialized_name="userAssignedIdentities",
            )

            user_assigned_identities = cls._schema_on_200.identity.user_assigned_identities
            user_assigned_identities.Element = AAZObjectType()

            _element = cls._schema_on_200.identity.user_assigned_identities.Element
            _element.client_id = AAZStrType(
                serialized_name="clientId",
                flags={"read_only": True},
            )
            _element.principal_id = AAZStrType(
                serialized_name="principalId",
                flags={"read_only": True},
            )

            properties = cls._schema_on_200.properties
            properties.enable_diagnostics_support = AAZBoolType(
                serialized_name="enableDiagnosticsSupport",
            )
            properties.ip_address = AAZStrType(
                serialized_name="ipAddress",
                flags={"read_only": True},
            )
            properties.logging = AAZObjectType()
            properties.managed_resource_group = AAZStrType(
                serialized_name="managedResourceGroup",
            )
            properties.network_profile = AAZObjectType(
                serialized_name="networkProfile",
            )
            properties.nginx_version = AAZStrType(
                serialized_name="nginxVersion",
                flags={"read_only": True},
            )
            properties.provisioning_state = AAZStrType(
                serialized_name="provisioningState",
            )

            logging = cls._schema_on_200.properties.logging
            logging.storage_account = AAZObjectType(
                serialized_name="storageAccount",
            )

            storage_account = cls._schema_on_200.properties.logging.storage_account
            storage_account.account_name = AAZStrType(
                serialized_name="accountName",
            )
            storage_account.container_name = AAZStrType(
                serialized_name="containerName",
            )

            network_profile = cls._schema_on_200.properties.network_profile
            network_profile.front_end_ip_configuration = AAZObjectType(
                serialized_name="frontEndIPConfiguration",
            )
            network_profile.network_interface_configuration = AAZObjectType(
                serialized_name="networkInterfaceConfiguration",
            )

            front_end_ip_configuration = cls._schema_on_200.properties.network_profile.front_end_ip_configuration
            front_end_ip_configuration.private_ip_addresses = AAZListType(
                serialized_name="privateIPAddresses",
            )
            front_end_ip_configuration.public_ip_addresses = AAZListType(
                serialized_name="publicIPAddresses",
            )

            private_ip_addresses = cls._schema_on_200.properties.network_profile.front_end_ip_configuration.private_ip_addresses
            private_ip_addresses.Element = AAZObjectType()

            _element = cls._schema_on_200.properties.network_profile.front_end_ip_configuration.private_ip_addresses.Element
            _element.private_ip_address = AAZStrType(
                serialized_name="privateIPAddress",
            )
            _element.private_ip_allocation_method = AAZStrType(
                serialized_name="privateIPAllocationMethod",
            )
            _element.subnet_id = AAZStrType(
                serialized_name="subnetId",
            )

            public_ip_addresses = cls._schema_on_200.properties.network_profile.front_end_ip_configuration.public_ip_addresses
            public_ip_addresses.Element = AAZObjectType()

            _element = cls._schema_on_200.properties.network_profile.front_end_ip_configuration.public_ip_addresses.Element
            _element.id = AAZStrType()

            network_interface_configuration = cls._schema_on_200.properties.network_profile.network_interface_configuration
            network_interface_configuration.subnet_id = AAZStrType(
                serialized_name="subnetId",
            )

            sku = cls._schema_on_200.sku
            sku.name = AAZStrType(
                flags={"required": True},
            )

            system_data = cls._schema_on_200.system_data
            system_data.created_at = AAZStrType(
                serialized_name="createdAt",
                flags={"read_only": True},
            )
            system_data.created_by = AAZStrType(
                serialized_name="createdBy",
                flags={"read_only": True},
            )
            system_data.created_by_type = AAZStrType(
                serialized_name="createdByType",
                flags={"read_only": True},
            )
            system_data.last_modified_at = AAZStrType(
                serialized_name="lastModifiedAt",
                flags={"read_only": True},
            )
            system_data.last_modified_by = AAZStrType(
                serialized_name="lastModifiedBy",
                flags={"read_only": True},
            )
            system_data.last_modified_by_type = AAZStrType(
                serialized_name="lastModifiedByType",
                flags={"read_only": True},
            )

            tags = cls._schema_on_200.tags
            tags.Element = AAZStrType()

            return cls._schema_on_200


__all__ = ["Show"]