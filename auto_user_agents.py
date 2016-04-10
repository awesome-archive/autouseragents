#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: broono
# @Date:   2016-04-10
# @Last Modified by:   broono
# @Last Modified time: 2016-04-10
# @Email:  tosven.broono@gmail.com


import os
import random
import requests
from bs4 import BeautifulSoup


class AutoUserAgents(object):

    """
This is an easy tool to randomly generate browser/robot user-agents.
Thanks to http://www.useragentstring.com, without whose work this is not easy.
I know this script may be like redoing a wheel or of little use, but it'll
help to make life a little bit more friendly. And that is exactly what
programming is good at, especially for a more dynamic language, isn't it?
Any suggestions, never hesitate to tell me.

    """

    # Just some boring but essential initial setup work.
    def __init__(self, agent_type="browserlist"):
        self.THANKS = "http://www.useragentstring.com"
        self.AGENTS_URLS = {"Crawlerlist": self.THANKS + "/pages/Crawlerlist/",
                            "Browserlist": self.THANKS + "/pages/Browserlist/"}
        self.AGENT_TYPE = self.set_agent_type(agent_type)
        self.CACHED_FILE = os.path.join(
            os.getcwd(), self.AGENT_TYPE.lower() + ".txt")
        self.check_cached()
        self.AGENTS = self.parse_agents()

    #  check and set cache status
    def check_cached(self):
        self.BROWSER_CACHED = True if os.path.exists(
            self.CACHED_FILE) else False
        self.CRAWLER_CACHED = True if os.path.exists(
            self.CACHED_FILE) else False
        # if there exists a cache file then it's cached
        self.CACHED = True if (
            self.BROWSER_CACHED or self.CRAWLER_CACHED) else False

    #  check and set agent type, which starts with an capitalized letter
    def set_agent_type(self, agent_type="browserlist"):
        if agent_type.capitalize() in self.AGENTS_URLS.keys():
            return agent_type.capitalize()
        else:
            print "agent_type must be in ['browserlist','crawlerlist']"
            raise TypeError

    # a fast way to reset/refresh the agent list file,
    # can make an easy switch from one agent type to the other
    # agent_type can be"browserlist" or "crawlerlist"
    def reset(self, agent_type="browserlist"):
        if self.CACHED:  # if cached then delete cache file and parse again
            # set corresponding cache status to False
            if self.BROWSER_CACHED:
                self.BROWSER_CACHED = False
            if self.CRAWLER_CACHED:
                self.CRAWLER_CACHED = False
            os.remove(self.CACHED_FILE)  # remove cached file
            self.CACHED = False  # set overall cache status to False
            # reset agent type on module leve
            self.AGENT_TYPE = self.set_agent_type(agent_type)
            # reset corresponding cache file name
            self.CACHED_FILE = os.path.join(
                os.getcwd(), self.AGENT_TYPE.lower() + ".txt")
            self.AGENTS = self.parse_agents()  # let's roll :D
        else:  # if not cached then no need to reset
            print "{}.txt file not cached".format(self.CACHED_FILE)
            raise IOError

    # believe me it's really simple, just randomly choose one item and return
    def random_agent(self):
        length = len(self.AGENTS)
        random_id = random.randint(0, length - 1)
        return self.AGENTS[random_id]  # here we go :P

    # parse agents list
    def parse_agents(self):
        agent_list = []
        if self.CACHED:  # if cache file exists then open cache file and read
            with open(self.CACHED_FILE, "r") as f:
                for line in f.readlines():
                    agent = line.strip()
                    if agent not in ["", None]:
                        agent_list.append(agent)
        else:  # if cache file not exists then fetch data from internet
            # determine the data url according to agent type
            url = self.AGENTS_URLS[self.AGENT_TYPE]
            resp = requests.get(url)
            cont = resp.content
            html = cont.decode(resp.encoding).encode(
                "utf-8")  # change codec to utf-8
            soup = BeautifulSoup(html, "lxml")
            # find all tags with a li tag under the liste tree
            agent_list_tags = soup.find(
                "div", {"id": "liste"}).findAll("li")
            with open(self.CACHED_FILE, "w") as f:  # generate cache file
                for x in agent_list_tags:
                    agent = x.a.getText()  # agent name
                    f.write(agent + "\n")
                    agent_list.append(agent)  # agent list to return
            self.check_cached()  # recheck cache status
        return agent_list  # we're done

if __name__ == '__main__':
    myagent = AutoUserAgents()
    print myagent.random_agent()
