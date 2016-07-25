# This file is auto-generated from clustering.idl(0.6.4-33-gcc8d7ca) with jenerator version 0.8.5-6-g5a2c923/master
# *** DO NOT EDIT ***


import sys
import msgpack
import jubatus.common
from jubatus.common.types import *

class WeightedDatum:
  TYPE = TTuple(TFloat(), TDatum())

  def __init__(self, weight, point):
    self.weight = weight
    self.point = point

  def to_msgpack(self):
    t = (self.weight, self.point)
    return self.__class__.TYPE.to_msgpack(t)

  @classmethod
  def from_msgpack(cls, arg):
    val = cls.TYPE.from_msgpack(arg)
    return WeightedDatum(*val)

  def __repr__(self):
    gen = jubatus.common.MessageStringGenerator()
    gen.open("weighted_datum")
    gen.add("weight", self.weight)
    gen.add("point", self.point)
    gen.close()
    return gen.to_string()

