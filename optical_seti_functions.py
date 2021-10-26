def running_median(arr1, window_size):
    import numpy as np
    fluxes = np.array(arr1)
    median_iterations = len(arr1) - window_size + 1
    running_median = []
    for i in range(0, median_iterations):
        start = i 
        end = i + window_size
        running_median.append(np.median(fluxes[start:end])) 
    return(running_median)

def running_mean(arr1, window_size):
    import numpy as np
    fluxes = np.array(arr1)
    mean_iterations = len(fluxes) - window_size + 1
    running_mean = []
    for i in range(0, mean_iterations):
        start = i 
        end = i + window_size
        running_mean.append(np.mean(fluxes[start:end])) 
    return(running_mean)

def smoothed_spectrum(running_median, arr1):
   normalized_flux = arr1[500:(len(running_median) + 500)]/running_median
   return normalized_flux



def spike_searcher(normalized_flux):
    count = 0 #we set the count variable
    for i in range(len(normalized_flux)):
            if normalized_flux[i] >= 5:
                 count += 1
            else:
                if count >= 5 and count <= 500:
                    print(i - count, i)
                    count = 0

def original_spectrum_plot(wave, arr1, index1, index2):
    from matplotlib import pyplot as plt
    plt.plot(wave[index1:index2], arr1[index1:index2], '.-')

def flat_spectrum_plot(wave, normalized_flux, index1, index2):  
    from matplotlib import pyplot as plt
    plt.plot(wave[index1:index2], normalized_flux[index1:index2], '.-')

def median_spectrum_plot(wave, runing_median, index1, index2):
    from matplotlib import pyplot as plt
    plt.plot(wave[index1:index2],running_median[index1:index2], '.-')

def seti_spike_searcher(arr1, min_count = 5, max_count = 500, flux_threshold = 5):
    window_size = 1000
    continuum = running_median(arr1, window_size)
    normalized_flux = arr1[500:(len(continuum) + 500)]/continuum
    count = 0 #we set the count variable
    for i in range(len(normalized_flux)):
            if normalized_flux[i] >= flux_threshold:
                 count += 1
            else:
                if count >= min_count and count <= max_count:
                    print(i - count, i)
                    count = 0
#Put stricter upper limit to rule out broader



