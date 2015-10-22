A simple demo for [Fabric](http://docs.fabfile.org/en/1.10/).

## Fabric Installation

On Mac OSX:

If you don't already have `pip`:

```
sudo easy_install pip
```

Install Fabric:

```
sudo pip install fabric
```

## Usage:

Clone this repo, then `cd` into the `gdi` directory. Now you can list out the fabric tasks available to you using `fab -l`.

Try running commands! Like `fab speak`, `fab speak_custom:"hello everyone"`.

After that you can start building your own tasks.

If you want to run the `convert_mp3` task, you will need to install the mp3 converter `lame`. On Mac, simply do:

```
brew install lame
```

Then you can do `fab convert_mp3`. 


The rest of the commands are retained as reference. If you want to run remote commands, you can supply the configuration that has been commented out in the first few lines of `fabfile.py`.

Have fun and be in touch with any questions!
