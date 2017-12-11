from mcpi.minecraft import Minecraft
mc = Minecraft.create()

x = -114.6
y = 10
z = -25.6
gift = mc.getBlock(x, y, z)

if gift == 57:
    mc.setBlock(-113.6, 8, -25.6, 0)
else:
    mc.postToChat("Place an offering on the pedestal.")
