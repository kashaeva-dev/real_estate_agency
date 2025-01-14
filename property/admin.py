from django.contrib import admin
from django.utils.translation import gettext_lazy as _

from .models import Flat, Complaint, Owner


class PriceRangeListFilter(admin.SimpleListFilter):
    title = _('Цена квартиры')
    parameter_name = 'price'

    def lookups(self, request, model_admin):
        return (
            ('3000000', _('до 3 млн. руб.')),
            ('3000001', _('больше 3 млн. руб.')),
        )

    def queryset(self, request, queryset):
        if self.value() == '3000000':
            return queryset.filter(price__lte=3000000)
        if self.value() == '3000001':
            return queryset.filter(price__gt=3000000)


class FlatsInline(admin.StackedInline):
    model = Owner.flats.through
    raw_id_fields = ('owner', 'flat')


@admin.register(Flat)
class FlatAdmin(admin.ModelAdmin):
    search_fields = (
        'town',
        'address',
    )
    readonly_fields = [
        'created_at',
    ]
    list_display = (
        'town',
        'address',
        'price',
        'new_building',
        'construction_year',
    )
    list_editable = (
        'new_building',
    )
    list_filter = (
        PriceRangeListFilter,
        'new_building',
        'rooms_number',
    )
    raw_id_fields = (
        'likes',
    )
    inlines = [FlatsInline]


@admin.register(Complaint)
class ComplaintAdmin(admin.ModelAdmin):
    raw_id_fields = ('flat',)


@admin.register(Owner)
class OwnerAdmin(admin.ModelAdmin):
    raw_id_fields = ('flats',)
    inlines = [FlatsInline]
