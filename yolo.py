import os


def train(img, epochs, data, weights):
    command = r"python .\yolov5\train.py --img " + str(img) + " --epochs " + str(
        epochs) + " --data " + data + " --weights " + weights
    print(command)
    os.system(command)


def detect(weights, conf, source):
    command = r"python .\yolov5\detect.py --weights " + weights + " --conf " + str(conf) + " --source " + source
    print(command)
    os.system(command)


def validate(weights, data, img):
    command = r"python .\yolov5\val.py --weights " + weights + " --data " + data + " --img " + str(img)
    print(command)

    os.system(command)

def export(weights):
    command = r"python .\yolov5\export.py --weights " + weights + " --include pb "
    print(command)
    os.system(command)

def main():
    # # trenowanie
    # img = 416
    # epochs = 3
    # data = r".\dataset\data.yaml"
    # weights = r".\yolov5\yolov5s.pt"
    # train(img, epochs, data, weights)
    #
    # # detekcja
    conf = 0.25
    source = r".\dataset\my_dataset\test\images"

    # weights = r".\yolov5\runs\train\exp7\weights\best.pt"
    weights = r".\yolov5\runs\train\exp4\weights\best.pt"

    detect(weights, conf, source)
    #
    # # walidacja
    # weights = r".\yolov5\runs\train\exp4\weights\best.pt"
    # data = r".\dataset\data.yaml"
    # img = 416
    #
    # # # data = r".\dataset\my_dataset\data.yaml"
    # # img = 640
    #
    # validate(weights, data, img)

    # # wlasny zbior
    # img = 640
    # epochs = 50
    # data = r".\dataset\my_dataset\data.yaml"
    # weights = r".\yolov5\runs\train\exp7\weights\best.pt"
    # # train(img, epochs, data, weights)

    # export(weights)

if __name__ == '__main__':
    main()
