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
    "large-storage-instance create",
)
class Create(AAZCommand):
    """Create an Azure Large Storage Instance for the specified subscription,
resource group, and instance name.

    :example: Create an Azure Large Storage Instance
        az large-storage-instance create -g myResourceGroup -n myAzureLargeStorageInstance -l westus2 --sku S72
    """

    _aaz_info = {
        "version": "2024-08-01-preview",
        "resources": [
            ["mgmt-plane", "/subscriptions/{}/resourcegroups/{}/providers/microsoft.azurelargeinstance/azurelargestorageinstances/{}", "2024-08-01-preview"],
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
        _args_schema.instance_name = AAZStrArg(
            options=["-n", "--name", "--instance-name"],
            help="Name of the AzureLargeStorageInstance.",
            required=True,
            fmt=AAZStrArgFormat(
                pattern=".*",
            ),
        )
        _args_schema.resource_group = AAZResourceGroupNameArg(
            required=True,
        )

        # define Arg Group "Properties"

        _args_schema = cls._args_schema
        _args_schema.instance_id = AAZStrArg(
            options=["--alsi-id", "--instance-id"],
            arg_group="Properties",
            help="Specifies the AzureLargeStorageInstance unique ID.",
        )

        # define Arg Group "Resource"

        _args_schema = cls._args_schema
        _args_schema.identity = AAZObjectArg(
            options=["--identity"],
            arg_group="Resource",
            help="The managed service identities assigned to this resource.",
        )
        _args_schema.location = AAZResourceLocationArg(
            arg_group="Resource",
            help="The geo-location where the resource lives",
            required=True,
            fmt=AAZResourceLocationArgFormat(
                resource_group_arg="resource_group",
            ),
        )
        _args_schema.tags = AAZDictArg(
            options=["--tags"],
            arg_group="Resource",
            help="Resource tags.",
        )

        identity = cls._args_schema.identity
        identity.type = AAZStrArg(
            options=["type"],
            help="Type of managed service identity (where both SystemAssigned and UserAssigned types are allowed).",
            required=True,
            enum={"None": "None", "SystemAssigned": "SystemAssigned", "SystemAssigned,UserAssigned": "SystemAssigned,UserAssigned", "UserAssigned": "UserAssigned"},
        )
        identity.user_assigned_identities = AAZDictArg(
            options=["user-assigned-identities"],
            help="The set of user assigned identities associated with the resource. The userAssignedIdentities dictionary keys will be ARM resource ids in the form: '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ManagedIdentity/userAssignedIdentities/{identityName}. The dictionary values can be empty objects ({}) in requests.",
        )

        user_assigned_identities = cls._args_schema.identity.user_assigned_identities
        user_assigned_identities.Element = AAZObjectArg(
            nullable=True,
            blank={},
        )

        tags = cls._args_schema.tags
        tags.Element = AAZStrArg()

        # define Arg Group "StorageProperties"

        _args_schema = cls._args_schema
        _args_schema.generation = AAZStrArg(
            options=["--generation"],
            arg_group="StorageProperties",
            help="the kind of storage instance",
        )
        _args_schema.hardware_type = AAZStrArg(
            options=["--hardware-type"],
            arg_group="StorageProperties",
            help="the hardware type of the storage instance",
            enum={"Cisco_UCS": "Cisco_UCS", "HPE": "HPE", "SDFLEX": "SDFLEX"},
        )
        _args_schema.offering_type = AAZStrArg(
            options=["--offering-type"],
            arg_group="StorageProperties",
            help="the offering type for which the resource is getting provisioned",
        )
        _args_schema.billing_mode = AAZStrArg(
            options=["--billing-mode"],
            arg_group="StorageProperties",
            help="the billing mode for the storage instance",
        )
        _args_schema.azure_large_storage_instance_size = AAZStrArg(
            options=["--sku", "--azure-large-storage-instance-size"],
            arg_group="StorageProperties",
            help="the SKU type that is provisioned",
        )
        _args_schema.storage_type = AAZStrArg(
            options=["--storage-type"],
            arg_group="StorageProperties",
            help="the storage protocol for which the resource is getting provisioned",
        )
        _args_schema.workload_type = AAZStrArg(
            options=["--workload-type"],
            arg_group="StorageProperties",
            help="the workload for which the resource is getting provisioned",
        )
        return cls._args_schema

    def _execute_operations(self):
        self.pre_operations()
        self.AzureLargeStorageInstanceCreate(ctx=self.ctx)()
        self.post_operations()

    @register_callback
    def pre_operations(self):
        pass

    @register_callback
    def post_operations(self):
        pass

    def _output(self, *args, **kwargs):
        result = self.deserialize_output(self.ctx.vars.instance, client_flatten=True)
        return result

    class AzureLargeStorageInstanceCreate(AAZHttpOperation):
        CLIENT_TYPE = "MgmtClient"

        def __call__(self, *args, **kwargs):
            request = self.make_request()
            session = self.client.send_request(request=request, stream=False, **kwargs)
            if session.http_response.status_code in [200, 201]:
                return self.on_200_201(session)

            return self.on_error(session.http_response)

        @property
        def url(self):
            return self.client.format_url(
                "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.AzureLargeInstance/azureLargeStorageInstances/{azureLargeStorageInstanceName}",
                **self.url_parameters
            )

        @property
        def method(self):
            return "PUT"

        @property
        def error_format(self):
            return "MgmtErrorFormat"

        @property
        def url_parameters(self):
            parameters = {
                **self.serialize_url_param(
                    "azureLargeStorageInstanceName", self.ctx.args.instance_name,
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
                    "api-version", "2024-08-01-preview",
                    required=True,
                ),
            }
            return parameters

        @property
        def header_parameters(self):
            parameters = {
                **self.serialize_header_param(
                    "Content-Type", "application/json",
                ),
                **self.serialize_header_param(
                    "Accept", "application/json",
                ),
            }
            return parameters

        @property
        def content(self):
            _content_value, _builder = self.new_content_builder(
                self.ctx.args,
                typ=AAZObjectType,
                typ_kwargs={"flags": {"required": True, "client_flatten": True}}
            )
            _builder.set_prop("identity", AAZObjectType, ".identity")
            _builder.set_prop("location", AAZStrType, ".location", typ_kwargs={"flags": {"required": True}})
            _builder.set_prop("properties", AAZObjectType, typ_kwargs={"flags": {"client_flatten": True}})
            _builder.set_prop("tags", AAZDictType, ".tags")

            identity = _builder.get(".identity")
            if identity is not None:
                identity.set_prop("type", AAZStrType, ".type", typ_kwargs={"flags": {"required": True}})
                identity.set_prop("userAssignedIdentities", AAZDictType, ".user_assigned_identities")

            user_assigned_identities = _builder.get(".identity.userAssignedIdentities")
            if user_assigned_identities is not None:
                user_assigned_identities.set_elements(AAZObjectType, ".", typ_kwargs={"nullable": True})

            properties = _builder.get(".properties")
            if properties is not None:
                properties.set_prop("azureLargeStorageInstanceUniqueIdentifier", AAZStrType, ".instance_id")
                properties.set_prop("storageProperties", AAZObjectType)

            storage_properties = _builder.get(".properties.storageProperties")
            if storage_properties is not None:
                storage_properties.set_prop("generation", AAZStrType, ".generation")
                storage_properties.set_prop("hardwareType", AAZStrType, ".hardware_type")
                storage_properties.set_prop("offeringType", AAZStrType, ".offering_type")
                storage_properties.set_prop("storageBillingProperties", AAZObjectType)
                storage_properties.set_prop("storageType", AAZStrType, ".storage_type")
                storage_properties.set_prop("workloadType", AAZStrType, ".workload_type")

            storage_billing_properties = _builder.get(".properties.storageProperties.storageBillingProperties")
            if storage_billing_properties is not None:
                storage_billing_properties.set_prop("billingMode", AAZStrType, ".billing_mode")
                storage_billing_properties.set_prop("sku", AAZStrType, ".azure_large_storage_instance_size")

            tags = _builder.get(".tags")
            if tags is not None:
                tags.set_elements(AAZStrType, ".")

            return self.serialize_content(_content_value)

        def on_200_201(self, session):
            data = self.deserialize_http_content(session)
            self.ctx.set_var(
                "instance",
                data,
                schema_builder=self._build_schema_on_200_201
            )

        _schema_on_200_201 = None

        @classmethod
        def _build_schema_on_200_201(cls):
            if cls._schema_on_200_201 is not None:
                return cls._schema_on_200_201

            cls._schema_on_200_201 = AAZObjectType()

            _schema_on_200_201 = cls._schema_on_200_201
            _schema_on_200_201.id = AAZStrType(
                flags={"read_only": True},
            )
            _schema_on_200_201.identity = AAZObjectType()
            _schema_on_200_201.location = AAZStrType(
                flags={"required": True},
            )
            _schema_on_200_201.name = AAZStrType(
                flags={"read_only": True},
            )
            _schema_on_200_201.properties = AAZObjectType(
                flags={"client_flatten": True},
            )
            _schema_on_200_201.system_data = AAZObjectType(
                serialized_name="systemData",
                flags={"read_only": True},
            )
            _schema_on_200_201.tags = AAZDictType()
            _schema_on_200_201.type = AAZStrType(
                flags={"read_only": True},
            )

            identity = cls._schema_on_200_201.identity
            identity.principal_id = AAZStrType(
                serialized_name="principalId",
                flags={"read_only": True},
            )
            identity.tenant_id = AAZStrType(
                serialized_name="tenantId",
                flags={"read_only": True},
            )
            identity.type = AAZStrType(
                flags={"required": True},
            )
            identity.user_assigned_identities = AAZDictType(
                serialized_name="userAssignedIdentities",
            )

            user_assigned_identities = cls._schema_on_200_201.identity.user_assigned_identities
            user_assigned_identities.Element = AAZObjectType(
                nullable=True,
            )

            _element = cls._schema_on_200_201.identity.user_assigned_identities.Element
            _element.client_id = AAZStrType(
                serialized_name="clientId",
                flags={"read_only": True},
            )
            _element.principal_id = AAZStrType(
                serialized_name="principalId",
                flags={"read_only": True},
            )

            properties = cls._schema_on_200_201.properties
            properties.azure_large_storage_instance_unique_identifier = AAZStrType(
                serialized_name="azureLargeStorageInstanceUniqueIdentifier",
            )
            properties.storage_properties = AAZObjectType(
                serialized_name="storageProperties",
            )

            storage_properties = cls._schema_on_200_201.properties.storage_properties
            storage_properties.generation = AAZStrType()
            storage_properties.hardware_type = AAZStrType(
                serialized_name="hardwareType",
            )
            storage_properties.offering_type = AAZStrType(
                serialized_name="offeringType",
            )
            storage_properties.provisioning_state = AAZStrType(
                serialized_name="provisioningState",
                flags={"read_only": True},
            )
            storage_properties.storage_billing_properties = AAZObjectType(
                serialized_name="storageBillingProperties",
            )
            storage_properties.storage_type = AAZStrType(
                serialized_name="storageType",
            )
            storage_properties.workload_type = AAZStrType(
                serialized_name="workloadType",
            )

            storage_billing_properties = cls._schema_on_200_201.properties.storage_properties.storage_billing_properties
            storage_billing_properties.billing_mode = AAZStrType(
                serialized_name="billingMode",
            )
            storage_billing_properties.sku = AAZStrType()

            system_data = cls._schema_on_200_201.system_data
            system_data.created_at = AAZStrType(
                serialized_name="createdAt",
            )
            system_data.created_by = AAZStrType(
                serialized_name="createdBy",
            )
            system_data.created_by_type = AAZStrType(
                serialized_name="createdByType",
            )
            system_data.last_modified_at = AAZStrType(
                serialized_name="lastModifiedAt",
            )
            system_data.last_modified_by = AAZStrType(
                serialized_name="lastModifiedBy",
            )
            system_data.last_modified_by_type = AAZStrType(
                serialized_name="lastModifiedByType",
            )

            tags = cls._schema_on_200_201.tags
            tags.Element = AAZStrType()

            return cls._schema_on_200_201


class _CreateHelper:
    """Helper class for Create"""


__all__ = ["Create"]