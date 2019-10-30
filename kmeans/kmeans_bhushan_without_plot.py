import math
import copy

# init centroids and clusters
clusters, centroids = {}, {}

def euclid(p1, p2):
    return math.hypot(p2[0] - p1[0], p2[1] - p1[1])

def print_output(clusters, centroids, iteration):
    print(f'\nIteration: {iteration}')
    for ce, cl in zip(centroids, clusters):
        print(f'Centroid={centroids[ce]}: Cluster={clusters[cl]}')

def kmeans(data, k=2):
    # check the data is 2D or 1D
    dim = 2 if isinstance(data[0], tuple) else 1

    # assigning first k centroids
    for i in range(k):
        centroids[i] = data[i]
    
    iters = 0
    while True:
        for i in range(k):
            clusters[i] = []

        # classifying data into clusters
        for d in data:
            if dim == 2:
                dist = [euclid(d, centroids[c]) for c in centroids]
                clusters[dist.index(min(dist))].append(d)
            else:
                dist = [abs(d-centroids[c]) for c in centroids]
                clusters[dist.index(min(dist))].append(d)
        
        # copying centroids into a variable for future check
        prev_centroids = copy.deepcopy(centroids)

        # updating centroids according to the new clusters
        for c in clusters:
            if dim == 1:
                centroids[c] = round(sum(clusters[c])/len(clusters[c]), 2)
            else:
                avg_x = round(sum( p[0] for p in clusters[c] ) / len(clusters[c]), 2)
                avg_y = round(sum( p[1] for p in clusters[c] ) / len(clusters[c]), 2)
                centroids[c] = (avg_x, avg_y)
        
        print_output(clusters, centroids, iters)
        iters += 1

        # stopping condition
        if prev_centroids == centroids:
            break


if __name__ == '__main__':
    data_1d = [2, 4, 10, 12, 11, 3, 30, 25, 20]
    data_2d = [(1,1), (2,1), (4,3), (5,4)]
    kmeans(data_2d)