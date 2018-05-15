from functools import partial
from django.forms.models import modelformset_factory


class QuickEditAdmin:
    quick_editable = ()

    def get_changelist_formset(self, request, **kwargs):
        """
        Returns the quickedit formset for the row
        """
        defaults = {
            'formfield_callback': partial(self.formfield_for_dbfield, request=request),
        }
        defaults.update(kwargs)
        fields = self.quick_editable + self.list_editable
        return modelformset_factory(
            self.model, self.get_changelist_form(request, fields=fields), extra=0,
            fields=fields, **defaults
        )
