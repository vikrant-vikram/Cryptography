Our cryptography methods are often block based which require memory storage and have a considerable gate footprint for their implementation. For devices with limited storage space and processing requirements, the requirements of many block-based symmetric encryption methods cannot be feasibly implement.

We thus get light-weight cryptography method, and which have a lower processing requirement, and memory and gate footprint. With this, for symmetric key encryption, we often replace block cipher with stream ciphers. For this we generate an almost infinitely long key stream based on a key value and an IV (initialisation vector). The incoming bit stream is then EX-ORed with the key stream, and this is sent with the IV. On the other side, the key stream is recreated, and EX-OR with the cipher stream. This created the original data.



Trivium is a Light Weight Stream Cipher and was created Christophe De Cannière and Bart Preneel, and has a low footprint for hardware. It uses an 80-bit key, and generates up to 2⁶⁴ bits of output, with an 80-bit IV.

The Trivium cryptography method has 288 bit states and uses three registers (A, B and C), of 93, 84 and 111 bits. The method for each state is:



The key and IV are loaded up initially as:



We initially run through four 288 bit shifts before we take an output (this is defined as the warm up phase). The following gives an example of the cipher:



Trivium has low requirements in hardware and only requir
