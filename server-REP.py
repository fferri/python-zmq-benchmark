import zmq
import numpy as np
import argparse

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--size", type=int, default=3, help="Size of the square matrix (NxN)")
    args = parser.parse_args()

    context = zmq.Context()
    socket = context.socket(zmq.REP)
    socket.bind("tcp://*:5555")

    print(f"Server listening on port 5555 with matrix size {args.size}x{args.size}")

    while True:
        message = socket.recv()
        # Compute pseudoinverse of a random NxN matrix
        mat = np.random.rand(args.size, args.size)
        pinv = np.linalg.pinv(mat)
        socket.send(b"OK")  # Dummy response

if __name__ == "__main__":
    main()
