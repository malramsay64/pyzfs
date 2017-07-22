from __future__ import absolute_import, division, print_function
from abc import ABCMeta, abstractmethod
from pprint import pprint
import os
import numpy as np

from ..parallel import mpiroot

class WavefunctionLoader(object):
    __metaclass__ = ABCMeta

    def __init__(self):
        self.wfc = None
        self.scan()
        self.info()

    @abstractmethod
    def scan(self):
        """Scan current directory, construct wavefunction object"""
        if mpiroot:
            print("\n{}: scanning current working directory {}...\n".format(
                self.__class__.__name__, os.getcwd()
            ))

    def load(self, iorbs):
        """Load read space KS orbitals to memory, store in wfc.iorb_psir_map."""
        if mpiroot:
            print("\n{}: loading orbitals into memory...\n".format(
                self.__class__.__name__
            ))

        counter = 0
        for iorb in iorbs:
            spin, band = self.wfc.iorb_sb_map[iorb]
            psir = self.retrieve(spin, band)
            psir = self.normalize(psir)
            self.wfc.iorb_psir_map[iorb] = psir

            counter += 1
            if counter >= len(iorbs) // 10:
                if mpiroot:
                    print("........")
                counter = 0

    @abstractmethod
    def retrieve(self, spin, band):
        pass

    def info(self):
        if mpiroot:
            wfc = self.wfc
            print("   nuwfcs = {}, ndwfcs = {}, nwfcs = {}".format(
                wfc.nuorbs, wfc.ndorbs, wfc.norbs
            ))
            for iorb in range(wfc.norbs):
                print("     spin = {}     band = {}     file = {}".format(
                    wfc.iorb_sb_map[iorb][0], wfc.iorb_sb_map[iorb][1], wfc.iorb_fname_map[iorb]
                ))
            print("\nSystem Overview:")
            print("  Cell: ")
            pprint(wfc.cell.__dict__, indent=4)
            print("  FFT Grid: ")
            pprint(wfc.ft.__dict__, indent=4)

    def normalize(self, psir):
        """Normalize VASP pseudo wavefunction."""
        assert psir.shape == (self.wfc.ft.n1, self.wfc.ft.n2, self.wfc.ft.n3)
        norm = np.sqrt(np.sum(np.abs(psir) ** 2) * self.wfc.cell.omega / self.wfc.ft.N)
        return psir / norm