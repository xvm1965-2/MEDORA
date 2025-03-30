from django.contrib import admin
from django.db import models
from .utils import get_clean_verbose_name
from django.forms import DateInput

# admin.site.site_header = "Banca Mediolanum (login)"  # Title on the login page
# admin.site.site_title = "Registro DORA"  # Title on the browser tab
# admin.site.index_title = "Registro DORA"  # Title on the admin index page

class CustomAdmin(admin.ModelAdmin):
    class Media:
        css = {'all': ('css/admin_custom.css',)}
        js = ['js/admin_tooltips.js']
    formfield_overrides = {
        models.DateField: {'widget': DateInput(format='%Y-%m-%d', attrs={'type': 'date'})},
    }
class CleanHeaderMixin:
    """
    Mixin-only version that can be combined with any admin class
    """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        # Create mapping of original field names to display methods
        field_map = {}
        new_display = []
        
        for field_name in self.list_display:
            if hasattr(self.model, field_name):
                field = self.model._meta.get_field(field_name)
                display_name = f'display_{field_name}'
                
                if not hasattr(self, display_name):
                    def make_display_func(fn):
                        def display_func(obj):
                            return str(getattr(obj, fn))
                        return display_func
                    
                    setattr(self, display_name, make_display_func(field_name))
                    getattr(self, display_name).short_description = \
                        field.verbose_name.split('(')[0].strip() if '(' in field.verbose_name else field.verbose_name
                
                field_map[field_name] = display_name
                new_display.append(display_name)
            else:
                new_display.append(field_name)
        
        # Update list_display
        self.list_display = tuple(new_display)
        
        # Update list_display_links to use display methods
        if self.list_display_links:
            new_links = []
            for link in self.list_display_links:
                if link in field_map:
                    new_links.append(field_map[link])
                else:
                    new_links.append(link)
            self.list_display_links = tuple(new_links)
        elif self.list_display:
            first_field = self.list_display[0]
            if first_field.startswith('display_'):
                # If first item is one of our display methods
                self.list_display_links = (first_field,)
            else:
                # Find the original field name
                for orig_name, display_name in field_map.items():
                    if display_name == first_field:
                        self.list_display_links = (display_name,)
                        break
                else:
                    self.list_display_links = (first_field,)

from .models import ThirdPartyVendor_B1_01_01
@admin.register(ThirdPartyVendor_B1_01_01)
class ThirdPartyVendorAdmin(CleanHeaderMixin, CustomAdmin):
    list_display = ('lei', 'entity_name', )
    # search_fields = ('lei', 'entity_name')
    # list_filter = ('entity_type', 'country_code')
 
from .models import FinancialEntity_B1_02
@admin.register(FinancialEntity_B1_02)
class FinancialEntityAdmin(CleanHeaderMixin, CustomAdmin):
    list_display = ('lei', 'entity_name', 'country_code', 'entity_type')
    # search_fields = ('lei', 'entity_name')
    # list_filter = ('entity_type', 'country_code')
   
from .models import Branch_B1_03
@admin.register(Branch_B1_03)
class BranchAdmin(CleanHeaderMixin, CustomAdmin):
    list_display = ('branch_code', 'branch_name', 'head_office_lei', 'branch_country')
    search_fields = ('branch_code', 'branch_name', 'head_office_lei')
    list_filter = ('branch_country',)

from .models import ContractAgreement_B2_01
@admin.register(ContractAgreement_B2_01)
class ContractAgreementAdmin(CleanHeaderMixin, CustomAdmin):
    list_display = ('contract_reference_number', 'contract_type', 'currency', 'estimated_annual_cost')
    search_fields = ('contract_reference_number',)
    list_filter = ('contract_type', 'currency')

from .models import ContractAgreementDetails_B2_02
@admin.register(ContractAgreementDetails_B2_02)
class ContractAgreementDetailsAdmin(CleanHeaderMixin, CustomAdmin):
    list_display = ('contract_reference_number', 'financial_entity_lei', 'tic_service_type', 'start_date', 'end_date')
    search_fields = ('contract_reference_number__contract_reference_number', 'financial_entity_lei__lei')
    list_filter = ('tic_service_type', 'data_retention', 'dependency_level')
    readonly_fields=('vendor_code_type',)

from .models import IntraGroupContractAgreement_B2_03
@admin.register(IntraGroupContractAgreement_B2_03)
class IntraGroupContractAgreementAdmin(CleanHeaderMixin, CustomAdmin):
    list_display = ('contract_reference_number', 'linked_contract_reference')
    search_fields = ('contract_reference_number', 'linked_contract_reference__contract_reference_number')
    list_filter = ('contract_reference_number',)
    

from .models import ContractSigningEntity_B3_01
@admin.register(ContractSigningEntity_B3_01)
class ContractSigningEntityAdmin(CleanHeaderMixin, CustomAdmin):
    list_display = ('contract_reference_number', 'signing_entity_lei')
    search_fields = ('contract_reference_number__contract_reference_number', 'signing_entity_lei')
    list_filter = ('contract_reference_number',)

from .models import ThirdPartyVendorSigning_B3_02
@admin.register(ThirdPartyVendorSigning_B3_02)
class ThirdPartyVendorSigningAdmin(CleanHeaderMixin, CustomAdmin):
    list_display = ('contract_reference_number', 'third_party_vendor_code', 'vendor_code_type')
    search_fields = ('contract_reference_number__contract_reference_number', 'third_party_vendor_code')
    list_filter = ('contract_reference_number',)
    readonly_fields = ('vendor_code_type',)

from .models import FinancialEntityServiceProvider_B3_03
@admin.register(FinancialEntityServiceProvider_B3_03)
class FinancialEntityServiceProviderAdmin(CleanHeaderMixin, CustomAdmin):
    list_display = ('contract_reference_number', 'service_provider_lei')
    search_fields = ('contract_reference_number__contract_reference_number', 'service_provider_lei__lei')
    list_filter = ('contract_reference_number',)

from .models import FinancialEntityServiceUsage_B4_01
@admin.register(FinancialEntityServiceUsage_B4_01)
class FinancialEntityServiceUsageAdmin(CleanHeaderMixin, CustomAdmin):
    list_display = ('contract_reference_number', 'financial_entity_lei', 'entity_nature', 'branch_code')
    search_fields = (
        'contract_reference_number__contract_reference_number',
        'financial_entity_lei__lei',
        'branch_code',
    )
    list_filter = ('entity_nature',)

from .models import ThirdPartyVendor_B5_01
@admin.register(ThirdPartyVendor_B5_01)
class ThirdPartyVendorAdmin(CleanHeaderMixin, CustomAdmin):
    list_display = ('vendor_code', 'code_type', 'legal_name', 'vendor_type', 'headquarters_country')
    search_fields = ('vendor_code', 'legal_name', 'latin_name', 'headquarters_country')
    list_filter = ('code_type', 'vendor_type', 'headquarters_country')

from .models import SupplyChain_B5_02
@admin.register(SupplyChain_B5_02)
class SupplyChainAdmin(CleanHeaderMixin, CustomAdmin):
    list_display = ('contract_reference_number', 'tic_service_type', 'vendor_code', 'position')
    search_fields = (
        'contract_reference_number__contract_reference_number',
        'vendor_code__vendor_code',
        'recipient_code',
    )
    list_filter = ('tic_service_type', 'position')

from .models import FunctionIdentification_B6_01
@admin.register(FunctionIdentification_B6_01)
class FunctionIdentificationAdmin(CleanHeaderMixin, CustomAdmin):
    list_display = ('function_id', 'function_name', 'financial_entity_lei', 'essentiality')
    search_fields = ('function_id', 'function_name', 'financial_entity_lei__lei')
    list_filter = ('essentiality', 'impact')

from .models import ServiceEvaluation_B7_01
@admin.register(ServiceEvaluation_B7_01)
class ServiceEvaluationAdmin(CleanHeaderMixin, CustomAdmin):
    list_display = ('contract_reference_number', 'vendor_code', 'tic_service_type', 'substitutability')
    search_fields = ('contract_reference_number__contract_reference_number', 'vendor_code__vendor_code')
    list_filter = ('tic_service_type', 'substitutability', 'impact')
    readonly_fields = ('code_type','vendor_code',)

from .models import Type_of_financial_entity
@admin.register(Type_of_financial_entity)
class TypeOfFinancialEntityAdmin(CustomAdmin):
    list_display = ('code', 'description')
    search_fields = ('code', 'description')

from .models import Currency
@admin.register(Currency)
class CurrencyAdmin(CustomAdmin):
    list_display = ('name', 'symbol', 'numeric_code')
 
from .models import ICTService
@admin.register(ICTService)
class ICTServiceAdmin(CustomAdmin):
    list_display = ('service_id', 'service_type', 'description')
    
from .models import Authority
@admin.register(Authority)
class AuthorityAdmin(CustomAdmin):
    list_display = ('code', 'description')