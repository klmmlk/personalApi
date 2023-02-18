#!/usr/bin/python3
# -*- coding:utf-8 -*-
"""
@author: Jiong.L
@time: 2023/2/18 10:22
"""
from fastapi import APIRouter, Path

znzmo = APIRouter(prefix='/znzmo')


@znzmo.get('/{username}')
async def v1(
        username: str = Path(..., min_length=5)
):

    return {"user": username}
