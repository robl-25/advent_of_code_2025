import bisect


with open('input.txt') as f:
    ranges_str = f.read().split('\n\n')[0]

ranges = []

for l in ranges_str.strip().split('\n'):
    start, end = l.strip().split('-')

    start, end = int(start), int(end)

    start_idx = next((i for i, r in enumerate(ranges) if start in r), None)
    end_idx = next((i for i, r in enumerate(ranges) if end in r), None)

    if start_idx is None and end_idx is not None:
        ranges[end_idx] = range(start, ranges[end_idx].stop)

    if start_idx is not None and end_idx is None:
        ranges[start_idx] = range(ranges[start_idx].start, end + 1)

    if start_idx is not None and end_idx is not None:
        new_start = min(start, ranges[start_idx].start)
        new_end = max(end + 1, ranges[end_idx].stop)
        new_range = range(new_start, new_end)

        if start_idx != end_idx:
            ranges.pop(end_idx)

        ranges.pop(start_idx)

        bisect.insort(ranges, new_range, key=lambda r: r.start)

    if start_idx is None and end_idx is None:
        new_range = range(start, end + 1)

        range_indexes_to_remove = [i for i, r in enumerate(ranges) if r.start >= new_range.start and r.stop <= new_range.stop]
        for idx in reversed(range_indexes_to_remove):
            ranges.pop(idx)

        bisect.insort(ranges, new_range, key=lambda r: r.start)

print(sum(len(r) for r in ranges))
