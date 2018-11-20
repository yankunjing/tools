#!/usr/bin/python3
# -*- coding: utf-8 -*-

import paramiko
import itertools

class SSHClient (paramiko.SSHClient):

    # 模块初始
    def __init__ (
        self,
        hostname,
        hostport,
        username,
        password
    ):
        super().__init__()
        self._hostname = hostname
        self._hostport = hostport
        self._username = username
        self._password = password


    # 建立连接
    def connect (self):
        self.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        super().connect(self._hostname, self._hostport, self._username, self._password)

    # 执行指令
    def run_command (self, command, callback = print):
        stdin, stdout, stderr = super().exec_command(
            command, bufsize=1
        )

        stdout_iter = iter(stdout.readline, '')
        stderr_iter = iter(stderr.readline, '')

        for out, err in itertools.zip_longest(stdout_iter, stderr_iter):
            if out: callback(out.strip())
            if err: callback(err.strip())

        return stdin, stdout, stderr
