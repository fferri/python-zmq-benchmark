import zmq
import numpy as np
import argparse

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--size", type=int, default=3, help="Matrix size (NxN)")
    parser.add_argument("--port", type=int, default=5555, help="Port to bind to")
    args = parser.parse_args()

    context = zmq.Context()
    socket = context.socket(zmq.ROUTER)
    socket.bind(f"tcp://*:{args.port}")

    print(f"ROUTER server listening on port {args.port} with matrix size {args.size}x{args.size}")

    while True:
        # Receive: [identity, payload]
        identity, payload = socket.recv_multipart()

        # Simulate CPU work
        matrix = np.random.rand(args.size, args.size)
        _ = np.linalg.pinv(matrix)

        # Send back response: [identity, reply]
        socket.send_multipart([identity, b'OK'])

if __name__ == "__main__":
    main()
