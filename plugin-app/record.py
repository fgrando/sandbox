#!/bin/python3

class Record:
    def __init__(self):
        self._contents = []
        self._headers = []
        self.load('dummy')

    def load(self, filepath):
        data = {
            '1000': {'text':'text123', 'id': '1000', 'parents': '' },
            '1001': {'text':'lalalaasdf', 'id': '1001', 'parents': '' },
            '1002': {'text':'sdfg dgdf gdfg df g', 'id': '1002', 'parents': '' },
            '1003': {'text':'345 dferf w23r2fr', 'id': '1003', 'parents': '' },
            '1004': {'text':'fergrar fra frfa rf', 'id': '1004', 'parents': '' },
            '1005': {'text':'radio due', 'id': '1005', 'parents': '' },
        }

        for k in data.keys():
            self._contents.append(data[k])

        self._headers = list(self._contents[0].keys())

    def contents(self):
        return self._contents

    def headers(self):
        return self._headers

    def set_headers(self, headers):
        before = set(self._headers)
        if before == set(headers):
            self._headers = headers[:]
        else:
            print(f"cannot update headers from {self._headers} to {headers}")