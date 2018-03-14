#! /usr/bin/env python
# -*- coding: utf-8 -*-
#定义动物类
class Animals:

    """动物类"""
    def __init__(self, animal_factory=None):

        """动物工厂作为抽象工厂，可以随意设置"""
        self.Dogfactory = animal_factory

    def show_pet(self):

        """使用抽象工厂创建一个宠物并显示"""
        pet = self.Dogfactory.get_pet()
        print ("我是只可爱的{}".format(pet))

#animal生产工厂
class DogFactory:

    def get_pet(self):
        return Dog()

#抽象工厂的实例化
class Dog:

    def speak(self):
        return "旺旺"

    def __str__(self):
        return "dog"

#创建工厂
def get_factory():

    return DogFactory

if __name__ == '__main__':

    shop = Animals(get_factory)
    shop.show_pet()
