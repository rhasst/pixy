%module pixy

%include "stdint.i"
%include "carrays.i"
%include "cpointer.i"

%{
#define SWIG_FILE_WITH_INIT
#include "pixy.h"
%}

%array_class(struct Block, BlockArray);
%pointer_class(struct Frame, FramePtr);

int pixy_init();
int pixy_get_blocks(uint16_t max_blocks, BlockArray *blocks);
void pixy_close();
int pixy_command(const char *name, ...);
int pixy_rcs_get_position(uint8_t channel);
int pixy_rcs_set_position(uint8_t channel, uint16_t position);
int pixy_get_frame(FramePtr *frame);

struct Block
{
  uint16_t type;
  uint16_t signature;
  uint16_t x;
  uint16_t y;
  uint16_t width;
  uint16_t height;
  int16_t  angle;
};

struct Frame
{
  uint8_t* videodata;
  int32_t response;
  int32_t fourccc;
  int8_t renderflags;
  uint16_t xwidth;
  uint16_t ywidth;
  uint32_t size;
};