from mcpi.minecraft import Minecraft
mc = Minecraft.create()

buildX = 58
buildY = 17
buildZ = 36
width = 10
height = 5
length = 6

pos = mc.player.getTilePos()
x = pos.x
y = pos.y
z = pos.z

inside = buildX < x < buildX + width and buildZ < z < buildZ + length and buildY < y < buildY + height

mc.postToChat(int(inside))
