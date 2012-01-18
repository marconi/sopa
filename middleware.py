# -*- coding: utf-8 -*-

from django.template.context import RequestContext
from django.shortcuts import render_to_response


class SopaMiddleware(object):
    def process_request(self, request):
        return render_to_response('sopa/sopa.html', {}, RequestContext(request))
