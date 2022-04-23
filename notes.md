# Notes and discoveries

This file is to keep any notes and links about the board.

- [Product page](https://shop.sb-components.co.uk/products/stackypi?_pos=1&_sid=7ecd982d7&_ss=r)
- [Kickstarter page](https://www.kickstarter.com/projects/1415622428/pico-zero-rp2040-pico-based-board-on-pi-zero-form-factor)
- [GitHub repo](https://github.com/sbcshop/StackyPi)

## Specifications

### Memory
Although the SB Components marketing video and product pages confusingly list the board as having 64 MB / 64 Mb (note the mixed up capitalisation) of flash, this is *not 64 megabytes*.

- The [schematic](https://cdn.shopify.com/s/files/1/1217/2104/files/StackyPi-Schematic-File.pdf?v=1649228172) shows a 25Q128FV flash chip (128 megabits -> 16 megabytes).
- The board [in reality](images/flash.jpeg) has a [Winbond 25Q64JV chip](https://www.winbond.com/hq/product/code-storage-flash-memory/serial-nor-flash/?__locale=en&partNo=W25Q64JV) (64 megabits -> 8 megabytes).

Conclusion - *StackyPi has 8 megabytes (8 MB) of flash*.

### Firmware

Boards have apparently been shipped with differing builds of MicroPython (1.15 and 1.17 are known)

## Reviews and write-ups

- [Review on Tom's Hardware](https://www.tomshardware.com/reviews/sb-components-stackypi)
- [YouTube Review](https://www.youtube.com/watch?v=6nFzbBchgRI)

## Useful MicroPython drivers

## Supported HATs

If you have tried a Pi HAT or add-on, let us know!

- Pi Cube HAT (SB Components): the StackyPi repo has a sample for this.
