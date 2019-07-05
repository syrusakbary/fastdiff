import os
from wasmer import Instance

__dir__ = os.path.dirname(os.path.realpath(__file__))
wasm_file_location = os.path.join(__dir__, "fastdiff.wasm")


# Instantiates the module.
def initiate_instance():
    wasm_bytes = open(wasm_file_location, 'rb').read()
    instance = Instance(wasm_bytes)
    return instance

_instance = None


def get_instance():
    global _instance
    if _instance is None:
        _instance = initiate_instance()
    return _instance


def allocate_cstr(string, instance):
    subject = bytes(string, 'utf-8')
    length = len(subject)
    pointer = instance.exports.allocate(length)

    # Write the subject into the memory.
    memory = instance.memory.uint8_view(pointer)

    for nth in range(0, length):
        memory[nth] = subject[nth]

    # C-string terminates by NULL.
    memory[length] = 0

    return pointer, length


def get_cstr(pointer, instance):
    memory = instance.memory.uint8_view(pointer)
    memory_length = len(memory)
    nth = 0
    # for byte in memory:
    #     byte = memory[nth]
    #     if byte == 0:
    #         break
    #     yield byte
    while nth < memory_length:
        byte = memory[nth]
        if byte == 0:
            break
        yield byte
        nth += 1


def compare(first, second):
    instance = get_instance()
    # Allocate memory for the subject, and get a pointer to it.
    first_pointer, first_length = allocate_cstr(first, instance)
    second_pointer, second_length = allocate_cstr(second, instance)

    output_pointer = instance.exports.compare(first_pointer, second_pointer)

    output_bytes = bytes(get_cstr(output_pointer, instance))
    return output_bytes.decode().splitlines()

    # Deallocate the subject, and the output.
    instance.exports.deallocate(first_pointer, first_length)
    instance.exports.deallocate(second_pointer, second_length)
    instance.exports.deallocate(output_pointer, length_of_output)


_instance = get_instance()
