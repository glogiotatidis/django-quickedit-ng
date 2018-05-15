Quick Edit NG Documentation
==============================

:Authors:
   Corey Oordt
   Justin Quick <justquick@gmail.com>,
   Giorgos Logiotatidis <giorgos@sealabs.net>,
:Version: 0.2


::

    pip install django-quickedit-ng==0.2.0

Django Quick Edit NG is a way to quickly edit fields in a model directly from
the admin change_list view. It adds to the functionality of ``list_editable``
and allows for data entry in a drop down form in addition to inline. This
concept was borrowed from Wordpress and adapted into the Django admin interface.
Here is an example screenshot to show functionality

.. image:: http://github.com/glogiotatidis/django-quickedit-ng/raw/master/screenshot.png


About the fork
--------------

`Quick Edit <https://github.com/callowayproject/django-quickedit/>`_ was
originally a project from Corey and Justin. According to the GitHub repo the
project hasn't been updated for 8 years. After receiving no replies on the issue
asking whether the initial authors are interested to update the project, Giorgos
made the necessary changes to make this work with recent versions of Django and
published this package as `django-quickedit-ng`.


Installation and configuration
------------------------------

Include `quickedit` in the list of your installed apps. For each `ModelAdmin`
you want to get quick edit, inherit `QuickEditAdmin` and add the set of fields
you want to edit in a drop down in `quick_editable` variable.

Example::

  from django.contrib import admin
  from quickedit.admin import QuickEditAdmin

  class ArticleAdmin(QuickEditAdmin, admin.ModelAdmin):
      list_display = ('id', 'name', 'published')
      list_editable = ('published',)
      quick_editable = ('name',)

  admin.site.register(models.Article, ArticleAdmin)
