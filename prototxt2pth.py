from caffe2pth.caffenet import *
#import caffe.proto.caffe_pb2 as caffe_pb2

YOUT_PROTOTXT_PATH = 'pedestrian-and-vehicle-detector-adas-0001.prototxt' 

net = CaffeNet(YOUT_PROTOTXT_PATH)

torch.save(net, 'pedestrian-and-vehicle-detector-adas-0001.pth')

#net.load_state_dict(torch.load(OUTPUT_PTHMODEL_PATH))
