from mcpi.minecraft import Minecraft
mc = Minecraft.create()
x = -113
y = 29
z = 36
blockType = 103
mc.setBlock(x, y, z, blockType)
mc.setBlock(x, y + 1, z, blockType)
