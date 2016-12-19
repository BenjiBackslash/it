import daemon

from .runner import Runner

sleep_minutes = 4*60


def run_daemon():
    with daemon.DaemonContext():
        Runner().run(sleep_minutes)

if __name__ == '__main__':
    run_daemon()


