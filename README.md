# Cache-Simulator

Run the simulator as follows:

python my_cache_simulator.py fileName L1_Blocks l1_Size L2_Blocks L2_Size

eg. python my_cache_simulator.py heapsort.addr 16 16 64 64 
The output will be displayed as follows:

* L1 Hits: 	975926
* L1 Misses: 	144687
* L2 Hits: 	121523
* L2 Misses: 	23164
* Cycles: 	45075560

If you only want L1 cache and not L2, simply set the L2 variables to 0,

eg. python my_cache_simulator.py heapsort.addr 16 16 0 0

* L1 Hits: 	975926
* L1 Misses: 	144687
* Cycles: 	154446260
