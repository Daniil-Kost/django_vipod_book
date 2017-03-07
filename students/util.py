# -*- coding: utf-8 -*-
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.utils.translation import ugettext as _

def paginate(objects, size, request, context, var_name='object_list'):
	"""Paginate objects provided by view"""

	#apply pagination
	paginator =Paginator(objects, size)

	#try to get page number from request
	page =request.GET.get('page', '1')
	try:
		object_list =paginator.page(page)

	except PageNotAnInteger:
		#if page is not at integer, deliver first page
		object_list =paginator.page(1)

	except EmptyPage:
		#if page is out of range
		#deliver last page of results
		object_list =paginator.page(paginator.num_pages)

	#set variables into context
	context[var_name] =object_list
	context['is_paginated'] =object_list.has_other_pages()
	context['page_obj'] =object_list
	context['paginator'] =paginator

	return context

def get_groups(request):
	"""Returns list of existing groups"""
	#deferred import of Group model to avoid cycled imports
	from .models import Group

	#get currently selected group
	cur_group =get_current_group(request)

	groups =[]
	for group in Group.objects.all().order_by('title'):
		groups.append({
			'id': group.id,
			'title': group.title,
			'leader': group.leader and (u'%s %s' % (
				group.leader.first_name, 
				group.leader.last_name)) or None,
			'selected': cur_group and cur_group.id ==group.id and True or False
			})

	return groups


def get_current_group(request):
	"""Returns currently selected group or None"""

	#we remember selected group in a cookie
	pk =request.COOKIES.get('current_group')

	if pk:
		from .models import Group
		try:
			group =Group.objects.get(pk =int(pk))
		except Group.DoesNotExist:
			return None
		else:
			return group
	else:
		return None


def get_lang(request):
  if request.COOKIES.get('django_language') == 'en':
     pk = 'English'
     return pk
  elif request.COOKIES.get('django_language') == 'uk':
     pk = 'Українська'
     return pk
  elif request.COOKIES.get('django_language') == 'ru':
     pk = 'Русский'
     return pk 
  else:
  	 pk = 'Українська'
  	 return pk
 
	