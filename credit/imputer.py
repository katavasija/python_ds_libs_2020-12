class FeatureImputer:
    """Заполнение пропусков и обработка выбросов"""
    def __init__(self, X, method):
        assert method in ['01', '03a', '01_nan'], 'Неверный метод обработки'
        self._X = X.copy()
        self.method = method
        self.medians = X.median()
    
    def transform(self):
        if self.method == '01':
            self._t01()
        elif self.method == '03a':
            self._t03a()
        elif self.method == '01_nan':    
            self._t01()
            self._fill_nans()
        
        return self._X
    
    def _t01(self):
        self._transform_credit_score()
    
    def _t03a(self):
        self._transform_credit_score()
        self._transform_current_loan()

    def _transform_credit_score(self):
        def calc_outlier_condition():
            return (self._X[feature_name] > 1000)
        
        # outliers
        feature_name = 'Credit Score'
        outlier_condition = calc_outlier_condition()
        outlier_rows_count = self._X[outlier_condition].shape[0]
        
        while (outlier_rows_count):
            self._X.loc[outlier_condition, feature_name] = self._X.loc[outlier_condition, feature_name] / 10
            outlier_condition = calc_outlier_condition()
            outlier_rows_count = self._X[outlier_condition].shape[0]
    
    def _transform_current_loan(self):
        def calc_outlier_condition():
            return (self._X[feature_name] > 10000000)
        
        feature_name = 'Current Loan Amount'
        outlier_condition = calc_outlier_condition()
        self._X.loc[outlier_condition, feature_name] = self._X.loc[outlier_condition, feature_name] = 10000000
    
    def _fill_nans(self):
        """заполнение пропусков"""
        NUM_FEATURE_NAMES = [ 'Annual Income', 'Tax Liens', 'Number of Open Accounts', 'Years of Credit History', \
                              'Maximum Open Credit', 'Number of Credit Problems', 'Months since last delinquent', 'Bankruptcies', \
                              'Current Loan Amount', 'Current Credit Balance', 'Monthly Debt', 'Credit Score'] 
        for fn in NUM_FEATURE_NAMES:
            self._X[fn].fillna(-1, inplace = True)
            self._X.loc[self._X[fn] == -1, fn] = self.medians[fn]
        
        