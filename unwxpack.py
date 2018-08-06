import os
import sys
import struct

class WxPackFile:
    name_length = 0
    name = ""
    offset = 0
    size = 0

def unpack():
    with open(sys.argv[1],"rb") as file:
        root = os.path.dirname(os.path.realpath(file.name))
        name = "/"+os.path.basename(os.path.realpath(file.name))

        #header
        first_mark = struct.unpack("B",file.read(1))[0]
        info1 = struct.unpack(">L",file.read(4))[0]
        index_info_length = struct.unpack(">L",file.read(4))[0]
        body_info_length = struct.unpack(">L",file.read(4))[0]
        last_mark = struct.unpack("B",file.read(1))[0]
        file_count = struct.unpack(">L",file.read(4))[0]

        print('first_mark = '+ str(first_mark) + '\tinfo1 = '+str(info1)+'\tindex_info_length = '+ str(index_info_length) + '\nbody_info_length = ' + str(body_info_length)+'\nlast_mark = '+ str(last_mark)+'\tfile_count = '+ str(file_count))

        if (first_mark != 190 or last_mark != 237):
            print("is not wxapack!")
            exit()

        #index
        file_list = []

        for i in range(file_count):
            data = WxPackFile()

            data.name_length = struct.unpack(">L",file.read(4))[0]
            data.name = file.read(data.name_length)
            data.offset = struct.unpack(">L",file.read(4))[0]
            data.size = struct.unpack(">L",file.read(4))[0]

            file_list.append(data)

        #write data


        for dt in file_list:
            path = root + name + "unpack"+os.path.dirname(dt.name)
            dt.name = os.path.basename(dt.name)

            if not( os.path.exists(path)):
                os.makedirs(path)

            with open(path+"/"+dt.name,"wb") as f:
                file.seek(dt.offset)
                f.write(file.read(dt.size))

            print("path : " + path + "\tname : " + dt.name)




if __name__ == '__main__':
    print("start unpack:")

    unpack()

    print("finish unpack")
