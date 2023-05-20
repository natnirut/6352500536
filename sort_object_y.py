obj_detected = {'bottle': [110, 30], 'glass': [60, 35], 'book': [310, 23], 'phone': [90, 33], 'pen': [155, 100], 'mouse':
[200, 45], 'remote': [298, 165], 'fan': [300, 36]}
obj_detected.items()
sort_by_value = sorted( obj_detected.items(), key=lambda x: x[1], reverse=False)
sort_by_value


