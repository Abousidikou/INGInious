# -*- coding: utf-8 -*-
#
# This file is part of INGInious. See the LICENSE and the COPYRIGHTS files for
# more information about the licensing of this file.

import gettext


class I18nManager:

    def __init__(self, session_func):
        self.translations = {}
        self._session_func = session_func

    @property
    def _session(self):
        return self._session_func()

    def get_translation_obj(self, lang=None):
        if lang is None:
            lang = self._session.get("language", "")
        return self.translations.get(lang, gettext.NullTranslations())

    def gettext(self, *args, **kwargs):
        return self.get_translation_obj().gettext(*args, **kwargs)