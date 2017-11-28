from mcpi.minecraft import Minecraft
mc = Minecraft.create()

pos = mc.player.getTilePos()
x = pos.x
y = pos.y
z = pos.z

height = 2
blockType = 1

sideHeight = height
mc.setBlocks(x + 1, z + 1, x + 3, y + sideHeight - 1, z +3, blockType)

pointHeight = 5
mc.setBlocks(x + 2, y, z + 2, x + 2, y + pointHeight - 1, z + 2, blockType)

baseHeight = 2
mc.setBlock(x, y, x + 4, y + baseHeight - 1, z + 4, blockType)

