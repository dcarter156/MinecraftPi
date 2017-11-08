from mcpi.minecraft import Minecraft

mc= Minecraft.create()
Id= 17
x=10
y=11
z=12
x, y, z = mc.player.getPos()
mc.player.setPos(x, y+100, z) 
