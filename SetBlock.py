from mcpi.minecraft import Minecraft
from time import sleep

mc = Minecraft.create()

tnt = 46

x, y, z = mc.player.getPos()
mc.setBlock(x+11, y+11, z+11, tnt, 1)
