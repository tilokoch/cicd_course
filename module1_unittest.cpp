#include <gtest/gtest.h>
#include "module1.h"

namespace {

    TEST(module1_test, printMoin_test) {
        EXPECT_EQ("Moin", printMoin());
    }


}
