from django.contrib import admin

# Register your models here.

from django.contrib import admin
from .models import ThirdPartyVendor_B1_01_01

from django.contrib import admin

# admin.site.site_header = "Banca Mediolanum (login)"  # Title on the login page
# admin.site.site_title = "Registro DORA"  # Title on the browser tab
# admin.site.index_title = "Registro DORA"  # Title on the admin index page


@admin.register(ThirdPartyVendor_B1_01_01)
class ThirdPartyVendorAdmin(admin.ModelAdmin):
    list_display = ('lei', 'entity_name', 'country_code', 'entity_type')
    # search_fields = ('lei', 'entity_name')
    # list_filter = ('entity_type', 'country_code')



from .models import FinancialEntity_B1_02

@admin.register(FinancialEntity_B1_02)
class FinancialEntityAdmin(admin.ModelAdmin):
    list_display = ('lei', 'entity_name', 'country_code', 'entity_type')
    # search_fields = ('lei', 'entity_name')
    # list_filter = ('entity_type', 'country_code')


from .models import Type_of_financial_entity

@admin.register(Type_of_financial_entity)
class TypeOfFinancialEntityAdmin(admin.ModelAdmin):
    list_display = ('code', 'description')
    search_fields = ('code', 'description')

from .models import Branch_B1_03
@admin.register(Branch_B1_03)
class BranchAdmin(admin.ModelAdmin):
    list_display = ('branch_code', 'branch_name', 'head_office_lei', 'branch_country')
    search_fields = ('branch_code', 'branch_name', 'head_office_lei')
    list_filter = ('branch_country',)

from .models import ContractAgreement_B2_01

@admin.register(ContractAgreement_B2_01)
class ContractAgreementAdmin(admin.ModelAdmin):
    list_display = ('contract_reference_number', 'contract_type', 'currency', 'estimated_annual_cost')
    search_fields = ('contract_reference_number',)
    list_filter = ('contract_type', 'currency')


from .models import ContractAgreementDetails_B2_02

@admin.register(ContractAgreementDetails_B2_02)
class ContractAgreementDetailsAdmin(admin.ModelAdmin):
    list_display = ('contract_reference_number', 'financial_entity_lei', 'tic_service_type', 'start_date', 'end_date')
    search_fields = ('contract_reference_number__contract_reference_number', 'financial_entity_lei__lei')
    list_filter = ('tic_service_type', 'data_retention', 'dependency_level')

from .models import IntraGroupContractAgreement_B2_03

@admin.register(IntraGroupContractAgreement_B2_03)
class IntraGroupContractAgreementAdmin(admin.ModelAdmin):
    list_display = ('contract_reference_number', 'linked_contract_reference')
    search_fields = ('contract_reference_number', 'linked_contract_reference__contract_reference_number')
    list_filter = ('contract_reference_number',)


from .models import ContractSigningEntity_B3_01

@admin.register(ContractSigningEntity_B3_01)
class ContractSigningEntityAdmin(admin.ModelAdmin):
    list_display = ('contract_reference_number', 'signing_entity_lei')
    search_fields = ('contract_reference_number__contract_reference_number', 'signing_entity_lei')
    list_filter = ('contract_reference_number',)


from .models import ThirdPartyVendorSigning_B3_02
@admin.register(ThirdPartyVendorSigning_B3_02)
class ThirdPartyVendorSigningAdmin(admin.ModelAdmin):
    list_display = ('contract_reference_number', 'third_party_vendor_code', 'vendor_code_type')
    search_fields = ('contract_reference_number__contract_reference_number', 'third_party_vendor_code')
    list_filter = ('contract_reference_number',)

from .models import FinancialEntityServiceProvider_B3_03
@admin.register(FinancialEntityServiceProvider_B3_03)
class FinancialEntityServiceProviderAdmin(admin.ModelAdmin):
    list_display = ('contract_reference_number', 'service_provider_lei')
    search_fields = ('contract_reference_number__contract_reference_number', 'service_provider_lei__lei')
    list_filter = ('contract_reference_number',)


from .models import FinancialEntityServiceUsage_B4_01
@admin.register(FinancialEntityServiceUsage_B4_01)
class FinancialEntityServiceUsageAdmin(admin.ModelAdmin):
    list_display = ('contract_reference_number', 'financial_entity_lei', 'entity_nature', 'branch_code')
    search_fields = (
        'contract_reference_number__contract_reference_number',
        'financial_entity_lei__lei',
        'branch_code',
    )
    list_filter = ('entity_nature',)

from .models import ThirdPartyVendor_B5_01
@admin.register(ThirdPartyVendor_B5_01)
class ThirdPartyVendorAdmin(admin.ModelAdmin):
    list_display = ('vendor_code', 'code_type', 'legal_name', 'vendor_type', 'headquarters_country')
    search_fields = ('vendor_code', 'legal_name', 'latin_name', 'headquarters_country')
    list_filter = ('code_type', 'vendor_type', 'headquarters_country')

from .models import SupplyChain_B5_02
@admin.register(SupplyChain_B5_02)
class SupplyChainAdmin(admin.ModelAdmin):
    list_display = ('contract_reference_number', 'tic_service_type', 'vendor_code', 'position')
    search_fields = (
        'contract_reference_number__contract_reference_number',
        'vendor_code__vendor_code',
        'recipient_code',
    )
    list_filter = ('tic_service_type', 'position')

from .models import FunctionIdentification_B6_01
@admin.register(FunctionIdentification_B6_01)
class FunctionIdentificationAdmin(admin.ModelAdmin):
    list_display = ('function_id', 'function_name', 'financial_entity_lei', 'essentiality')
    search_fields = ('function_id', 'function_name', 'financial_entity_lei__lei')
    list_filter = ('essentiality', 'impact')

from .models import ServiceEvaluation_B7_01
@admin.register(ServiceEvaluation_B7_01)
class ServiceEvaluationAdmin(admin.ModelAdmin):
    list_display = ('contract_reference_number', 'vendor_code', 'tic_service_type', 'substitutability')
    search_fields = ('contract_reference_number__contract_reference_number', 'vendor_code__vendor_code')
    list_filter = ('tic_service_type', 'substitutability', 'impact')