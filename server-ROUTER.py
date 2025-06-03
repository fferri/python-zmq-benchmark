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
        # Receive the full ROUTER envelope: [identity, empty, data]
        parts = socket.recv_multipart()
        identity, empty, payload = parts

        # Simulate some CPU work
        matrix = np.random.rand(args.size, args.size)
        _ = np.linalg.pinv(matrix)

        # Reply with same identity envelope
        socket.send_multipart([identity, b'', b'OK'])

if __name__ == "__main__":
    main()
