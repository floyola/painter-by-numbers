from torchvision import datasets, models, transforms
from torch.utils.data import DataLoader, Dataset


def dataset(class_, bs_train=64, bs_valid=1, bs_test=1):
    '''
    Function that return the train, valid and test data
    
    Parameters
        class -> The type of the data that we want (ie, artist, style or genre)
        bs_train -> Batch size of the train data
        bs_valid -> Batch size of the valid data
        bs_test -> Batch size of the test data
    '''
    
    image_transforms = {
    'train': transforms.Compose([
        transforms.RandomResizedCrop(size=224),
        transforms.RandomHorizontalFlip(),
        transforms.ToTensor(),
        transforms.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225])
    ]),
    'valid': transforms.Compose([
        transforms.Resize(size=256),
        transforms.CenterCrop(size=224),
        transforms.ToTensor(),
        transforms.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225])
    ])
}
    train_directory = F'../data/{class_}/train'
    valid_directory = F'../data/{class_}/valid'
    test_directory = F'../data/{class_}/test'

    data = {
    'train': datasets.ImageFolder(root=train_directory, transform=image_transforms['train']),
    'valid': datasets.ImageFolder(root=valid_directory, transform=image_transforms['valid']),
    'test': datasets.ImageFolder(root=test_directory, transform=image_transforms['valid'])
     }

    # Size of Data, to be used for calculating Average Loss and Accuracy
    
    train_data_size = len(data['train'])
    test_data_size = len(data['test'])
    valid_data_size = len(data['valid'])
    
    print ('train:', train_data_size, 'valid:', valid_data_size, 'test:', test_data_size)

    dataloaders = {}

    # Create iterators for the Data loaded using DataLoader module
    dataloaders['train'] = DataLoader(data['train'], batch_size=bs_train, shuffle=True)
    dataloaders['test'] = DataLoader(data['test'], batch_size=bs_test, shuffle=True)
    dataloaders['valid'] = DataLoader(data['valid'],batch_size=bs_valid, shuffle=True)
    dataloaders['classes'] = {v: k for k, v in data['train'].class_to_idx.items()}
    return dataloaders
