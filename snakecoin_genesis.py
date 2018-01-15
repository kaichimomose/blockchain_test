from snakecoin_block import Block
import datetime as date


def create_genesis_block():
    return Block(0, date.datetime.now(), 'Gebesis Block', '0')
