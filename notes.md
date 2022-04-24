# Notes and discoveries

This file is to keep any notes and links about the board.

- [Product page](https://shop.sb-components.co.uk/products/stackypi?_pos=1&_sid=7ecd982d7&_ss=r)
- [Kickstarter page](https://www.kickstarter.com/projects/1415622428/pico-zero-rp2040-pico-based-board-on-pi-zero-form-factor)
- [GitHub repo](https://github.com/sbcshop/StackyPi)
- [SB Components wiki](https://learn.sb-components.co.uk/StackyPi)

## Specifications

### Memory / storage

Although the SB Components marketing video and product pages confusingly list the board as having 64 MB / 64 Mb (note the mixed up capitalisation) of flash, this is *not 64 megabytes*.

- The [schematic](https://cdn.shopify.com/s/files/1/1217/2104/files/StackyPi-Schematic-File.pdf?v=1649228172) shows a 25Q128FV flash chip (128 megabits -> 16 megabytes).
- The board [in reality](images/flash.jpeg) has a [Winbond 25Q64JV chip](https://www.winbond.com/hq/product/code-storage-flash-memory/serial-nor-flash/?__locale=en&partNo=W25Q64JV) (64 megabits -> 8 megabytes).

- a commenter on YouTube points out that this is known to SB Components! The wiki page does acknowledge it is bits, not bytes.

**Conclusion** - *StackyPi has 8 megabytes (8 MB) of flash*.

### Firmware

Boards have apparently been shipped with differing builds of MicroPython (1.15 and 1.17 are known)

There is currently no specific MicroPython board definition available. Matt Trentini [notes](https://twitter.com/matt_trentini/status/1517484553530580992) that it should be similar to [this alternative definition](https://github.com/micropython/micropython/pull/8505). Probably wants an SD setup like a Pyboard, as well?

## Reviews and write-ups

- [Review on Tom's Hardware](https://www.tomshardware.com/reviews/sb-components-stackypi)
- [YouTube Review](https://www.youtube.com/watch?v=6nFzbBchgRI)

## Useful MicroPython drivers

- sdcard
- button debouncing
- pin mapping?

## Supported HATs

If you have tried a Pi HAT or add-on, let us know!

- Pi Cube HAT (SB Components): the StackyPi repo has a sample for this.

## Compatible cases

Due to the placement of the micro-USB port, which is slightly out of alignment with the Raspberry Pi Zero equivalent layout, Pi cases cannot easily be used without modification.

3D printed cases are possible.

## Similar products

- [RedRobotics Pico2Pi](https://www.tindie.com/products/redrobotics/pico-2-pi-adapter-board/)

