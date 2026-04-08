import time
import psutil
import threading

class SystemProfiler:
    """
    A context manager that runs a background thread to track 
    peak CPU and RAM usage, along with total execution time.
    """
    def __init__(self, process_name="Data Pipeline"):
        self.process_name = process_name
        self.start_time = None
        self.keep_measuring = True
        self.max_cpu = 0.0
        self.max_ram = 0.0

    def _monitor(self):
        while self.keep_measuring:
            # Check CPU and RAM usage
            cpu = psutil.cpu_percent(interval=None)
            ram = psutil.virtual_memory().percent
            
            # Update peak values
            if cpu > self.max_cpu: self.max_cpu = cpu
            if ram > self.max_ram: self.max_ram = ram
            
            # Sleep briefly so the monitor doesn't eat CPU itself
            time.sleep(0.5)

    def __enter__(self):
        self.start_time = time.time()
        self.keep_measuring = True
        # Start the monitoring loop in a separate background thread
        self.monitor_thread = threading.Thread(target=self._monitor, daemon=True)
        self.monitor_thread.start()
        print(f"\n[PROFILER] Starting {self.process_name}...")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.keep_measuring = False
        self.monitor_thread.join()
        elapsed_time = time.time() - self.start_time
        
        print(f"\n{'='*50}")
        print(f" PROFILING REPORT: {self.process_name}")
        print(f"{'='*50}")
        print(f" Total Time : {elapsed_time / 60:.2f} minutes ({elapsed_time:.2f} seconds)")
        print(f" Peak CPU   : {self.max_cpu}%")
        print(f" Peak RAM   : {self.max_ram}% System Memory")
        print(f"{'='*50}\n")