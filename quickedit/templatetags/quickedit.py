from django.contrib.admin.templatetags.admin_list import (items_for_result, result_headers,
                                                          result_list)
from django.template import Library


register = Library()


def results(cl, request):
    qe = hasattr(cl.model_admin, 'quick_editable')
    if cl.formset:
        if qe:
            for res, form in zip(cl.result_list, cl.formset.forms):
                yield {
                    'fields': list(items_for_result(cl, res, form)),
                    'quickedit': form,
                }
        else:
            for res, form in zip(cl.result_list, cl.formset.forms):
                yield {
                    'fields': list(items_for_result(cl, res, form)),
                    'quickedit': None
                }
    else:
        if qe:
            for res in cl.result_list:
                yield {
                    'fields': list(items_for_result(cl, res, None)),
                    'quickedit': cl.model_admin.get_changelist_formset(request).form(instance=res),
                }
        else:
            for res in cl.result_list:
                yield {
                    'fields': list(items_for_result(cl, res, None)),
                    'quickedit': None,
                }


@register.inclusion_tag('quickedit/change_list_results.html', takes_context=True)
def qe_result_list(context, cl):
    data = result_list(cl)
    data.update({
        'qe_fields': cl.model_admin.quick_editable,
        'results': list(results(cl, context.request)),
    })

    return data
