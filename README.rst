python-escpos japenese wrapper
==================================

`python-escpos <https://github.com/python-escpos/python-escpos>`_ の日本語対応版 `python-escpos for japanese <https://github.com/lrks/python-escpos>`_ のメンテがされてないようなので、
JpInit と JpTextの部分だけをくくりだして、本家のラッパーとして動作させる感じ。

* 本家がpython3対応済みなので、python3でok
* TM-T883 のパラレルにusb変換でのみ動作確認
    * raspberry pi zero w につけて、systemd + socat での *Network* による

使い方
--------

.. code:: python

    from escposjp import Network

    p = Network(localhost)
    p.hw("INIT")
    p.JpInit()
    p.JpText("テスト")
    p.cut()
