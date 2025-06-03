import zmq
import argparse
import time

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--requests", type=int, default=100, help="Number of requests to send")
    parser.add_argument("--addr", type=str, default="tcp://127.0.0.1:5555", help="Server address")
    args = parser.parse_args()

    context = zmq.Context()
    socket = context.socket(zmq.DEALER)
    socket.connect(args.addr)

    print(f"Connecting to {args.addr}")
    print(f"Sending {args.requests} requests asynchronously...")

    # Send all requests
    start_time = time.time()
    for _ in range(args.requests):
        socket.send(b"GO")

    # Wait for all replies
    for _ in range(args.requests):
        _ = socket.recv()

    end_time = time.time()
    elapsed = end_time - start_time
    rate = args.requests / elapsed

    print(f"Elapsed time: {elapsed:.3f} seconds")
    print(f"Average rate: {rate:.2f} requests/sec")

if __name__ == "__main__":
    main()
