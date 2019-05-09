# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import logging
import requests
import json
from rasa_core_sdk import Action
import arxiv

logger = logging.getLogger(__name__)


def pretty_arxiv(query_results):
    text = []
    for q_ in query_results:
        text.append("- {}\n\t{}\n\t{}\t{}\n".format(q_['title'], q_['authors'], q_['published'][:10],
                                                 q_['links'][0]['href']))
    return '\n'.join(text)


class ActionSearchArxiv(Action):
    def name(self):
        # define the name of the action which can then be included in training stories
        return "action_search_arxiv"

    def run(self, dispatcher, tracker, domain):
        # what your action should do
        query = tracker.get_slot('theme')
        q = arxiv.query(query, sort_by="lastUpdatedDate", max_results=3)
        dispatcher.utter_message(pretty_arxiv(q))  # send the message back to the user
        return []