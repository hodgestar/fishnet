# fishnet

A thing with lots of holes for trawling through data scattered over multiple machines.

Uses [execnet](http://codespeak.net/execnet/) to connect to remote hosts.


## Installation

```
git clone https://github.com/hodgestar/fishnet.git``
pip install -e ./fishnet
```

## Configuration

Configuration is read from a YAML file named ``./fishnet.yaml`` in the working
directory:

```
$ cat fishnet.yaml

hosts:
  # list the hosts to run commands on here
  - 'one.example.com'
  - 'two.example.com'
```

## Usage

```
python -m fishnet.cmds.ls '/path/to/logs/foo*.log'
python -m fishnet.cmds.grep 'Error' '/path/to/logs/foo*.log'
```

## Todo

Figure out if this is going anywhere useful.